# Grounding: transcribed
# Source: DEG_LMM_bootstrap_pseudobulk.ipynb (author repo AkilaRanjith/Molecular-Signatures-of-Resilience...); code cells only (outputs stripped).

# ---- cell 1 ----
# ====================================================================
# MAST mixed-model DE for multiple cell types and comparisons
# - Works for LOW vs INT and INT vs HIGH 
# - Robust counts-layer detection for h5ad
# ====================================================================

suppressPackageStartupMessages({
  library(Matrix)
  library(dplyr)
  library(ggplot2)
  library(MAST)
  library(lme4)
  library(SingleCellExperiment)
  library(zellkonverter)
  library(data.table)
})

# --------------------
# CONFIG: edit as needed
# --------------------
# h5ad files (one per comparison)
H5AD_LOW_INT   <- "path/BA9_low_int.h5ad"
H5AD_INT_HIGH  <- "path/BA9_int_high.h5ad"

# output directories
OUT_LOW_INT    <- "path/low_int/"
OUT_INT_HIGH   <- "path/int_high/"

# column with disease group in colData(sc)
GROUP_COL      <- "Disease.Group"   # expected values like "low", "int", "high" (case-insensitive)

# covariates expected in colData(sc) for the model
COVARIATES     <- c("subject", "Age", "Sex", "total_counts")

# cell-type labels 
CLUSTERS <- c(
  "Astrocyte-GFAP-OSMR","Astrocyte-SLC1A2-WIF1","Astrocyte-SLC1A2-SMTN","Astrocyte-GFAP-VCAN","OPC",
  "Microglia-Reactive-CD163","Microglia-Homeostatic-CX3CR1","Oligodendrocyte-OPALIN",
  "Ex8:[RORB-TLL1-TMTC4]","Ex9:[RORB-TLL1-PCP4-MID1]","Ex16:[FEZF2-SYT6]","Ex13:[THEMIS-POSTN]",
  "Ex10:[RORB-TLL1-PCP4-TYR]","Ex14:|FEZF2-HTR2C]","Ex3:[CUX2-RORB-GLIS3-SV2C]","Ex15:[FEZF2-ADRA1A]",
  "Ex1:[CUX2-SERPINE2-LAMP5]","Ex2:[CUX2-RORB-GLIS3-LRRC2]","Ex18:[FEZF2-ZFHX3-SCUBE1]","Ex17:[FEZF2-ZFHX3-SEMA3D]",
  "Ex7:[RORB-GABRG1]","Ex4:[CUX2-RORB-COL5A2-CLMN]","Ex5:[RORB-CUX2-EYA4]","Ex12:[THEMIS-PRRX1]",
  "Ex6:[RORB-MME]","Ex11:[RORB-ADGRL4]","In2:[LHX6-PVALB-MEPE]","In17:[ADARB2-VIP-ABI3BP]",
  "In7:[LHX6-SST-B3GAT2]","In1:[LHX6-PVALB-CLMN]","In3:[LHX6-PVALB-COL15A1]","In6:[LHX6-SST-SLC9A2]",
  "In15:[ADARB2-VIP-DACH2]","In16:[ADARB2-VIP-TAC3-NRP1]","In14:[ADARB2-SEMA3C]","In19:[ADARB2-CALB2-SCML4]",
  "In18:[ADARB2-VIP-EXPH5]","In11:[ADARB2-LAMP5-KIT]","In4:[LHX6-SST-MSR1]","In9:[LHX6-SST-NPY]",
  "In5:[LHX6-SST-SPON1]","In8:[LHX6-SST-SEL1L3]","In12:[ADARB2-LAMP5-NDNF]","In13:[ADARB2-SYT6]",
  "In10:[LHX6-ADARB2-LAMP5-HCRTR2]"
)

# minimums
MIN_CELLS_PER_CT <- 20
FREQ_EXPRESSED   <- 0.15  #  background keep genes expressed in >=15% of cells

# --------------------
# Helpers
# --------------------
dir_create <- function(p) if (!dir.exists(p)) dir.create(p, recursive = TRUE, showWarnings = FALSE)

sanitize_tag <- function(x) gsub("[^A-Za-z0-9._-]+", "_", x)

pick_counts_layer <- function(sce) {
  candidates <- c("counts", "raw", "X", "unspliced")  # order of preference
  layer <- intersect(candidates, assayNames(sce))
  if (length(layer) == 0) {
    stop("No counts-like layer found. Looked for: ", paste(candidates, collapse = ", "),
         " | Found: ", paste(assayNames(sce), collapse = ", "))
  }
  layer[1]
}

assert_covariates <- function(sce, covars) {
  missing <- setdiff(covars, colnames(colData(sce)))
  if (length(missing)) stop("Missing required colData columns: ", paste(missing, collapse = ", "))
}

#  comparison runner
run_comparison <- function(
  h5ad_path,
  out_dir,
  clusters,
  group_col = GROUP_COL,
  ref_level,       # e.g., "int"
  test_level       # e.g., "low" or "high"
) {
  message("\n==== Running comparison on: ", h5ad_path,
          " | ref=", ref_level, " vs test=", test_level, " ====")
  dir_create(out_dir)

  sc <- readH5AD(h5ad_path)
  assert_covariates(sc, c(GROUP_COL, COVARIATES))

  # choose counts layer and set counts per subset later
  counts_layer <- pick_counts_layer(sc)

  for (ct in clusters) {
    message("\n--- Cell type: ", ct)
    idx <- which(sc$Author_Annotation == ct)
    if (length(idx) < MIN_CELLS_PER_CT) {
      warning("Skipping ", ct, " (only ", length(idx), " cells).")
      next
    }
    sce <- sc[, idx]

    # set counts and logcounts
    counts(sce)    <- assay(sce, counts_layer)
    logcounts(sce) <- log2(counts(sce) + 1)

    # upcast
    sca <- SceToSingleCellAssay(sce)

    # CDR
    cdr <- colSums(assay(sca) > 0)
    colData(sca)$cngeneson <- scale(cdr)

    # thresholding 
    thres <- thresholdSCRNACountMatrix(assay(sca), cutbins = NULL, nbins = 10,
                                       min_per_bin = 30, bin_by = "median")
    assays(sca, withDimnames = FALSE) <- list(thresh = thres$counts_threshold, tpm = assay(sca))

    # gene filter
    keep <- freq(sca) > FREQ_EXPRESSED
    if (sum(keep) < 10) {
      warning("Fewer than 10 expressed genes after filtering in ", ct, ". Skipping.")
      next
    }
    sca <- sca[keep, ]

    # build group factor (lowercase)
    graw <- tolower(as.character(colData(sca)[[group_col]]))
    fac  <- factor(graw)
    if (!(ref_level %in% levels(fac)) || !(test_level %in% levels(fac))) {
      warning("Levels missing in ", ct, " | have: ", paste(levels(fac), collapse = ", "),
              " | need: ", ref_level, ", ", test_level, ". Skipping.")
      next
    }
    fac <- stats::relevel(fac, ref = ref_level)
    colData(sca)$test <- fac
    contrast_name <- paste0("test", test_level)

    # filenames
    tag <- sanitize_tag(ct)
    rds_sca      <- file.path(out_dir, paste0(ref_level, "_vs_", test_level, "_", tag, "_sca.rds"))
    rds_zlm      <- file.path(out_dir, paste0(ref_level, "_vs_", test_level, "_", tag, "_zlm_mixed.rds"))
    csv_logfc    <- file.path(out_dir, paste0(ref_level, "_vs_", test_level, "_", tag, "_logFC_mixed.csv"))
    rds_summary  <- file.path(out_dir, paste0(ref_level, "_vs_", test_level, "_", tag, "_summarymixedLRT.rds"))
    csv_hurdle   <- file.path(out_dir, paste0(ref_level, "_vs_", test_level, "_", tag, "_mixed_Hurdle.csv"))

    saveRDS(sca, rds_sca)

    # confirm covariates have variance (won't stop, but warns)
    for (v in COVARIATES) {
      vv <- colData(sca)[[v]]
      if (all(is.na(vv)) || length(unique(na.omit(vv))) < 2) {
        warning("Covariate '", v, "' has <2 unique values or is NA-only in ", ct, ". Model may fail.")
      }
    }

    # model
    form <- ~ test + (1 | subject) + cngeneson + Age + Sex + total_counts
    zlm_mixed <- tryCatch({
      zlm(form, sca, method = "glmer", ebayes = FALSE)
    }, error = function(e) {
      warning("zlm failed for ", ct, ": ", conditionMessage(e)); return(NULL)
    })
    if (is.null(zlm_mixed)) next
    saveRDS(zlm_mixed, rds_zlm)

    # logFC
    logFC <- tryCatch(getLogFC(zlm_mixed), error = function(e) NULL)
    if (!is.null(logFC)) {
      # add which group is upregulated by sign convention (positive => test > ref)
      logFC$Upregulated_in <- ifelse(logFC$logFC > 0, test_level, ref_level)
      write.csv(logFC, csv_logfc, row.names = FALSE)
    } else {
      warning("getLogFC failed for ", ct)
    }

    # LRT
    summary_mixed <- tryCatch({
      summary(zlm_mixed, doLRT = contrast_name)
    }, error = function(e) {
      warning("summary(doLRT=) failed for ", ct, ": ", conditionMessage(e)); return(NULL)
    })
    if (is.null(summary_mixed)) next
    saveRDS(summary_mixed, rds_summary)
    dt <- summary_mixed$datatable

    fcHurdle <- merge(
      dt[contrast == contrast_name & component == "H", .(primerid, `Pr(>Chisq)`)],
      dt[contrast == contrast_name & component == "logFC", .(primerid, coef, ci.hi, ci.lo)],
      by = "primerid"
    )
    fcHurdle[, fdr := p.adjust(`Pr(>Chisq)`, method = "fdr")]
    setorder(fcHurdle, fdr)

    # add Upregulated_in using coef sign from the continuous part
    fcHurdle[, Upregulated_in := ifelse(coef > 0, test_level, ref_level)]

    write.csv(fcHurdle, csv_hurdle, row.names = FALSE)
    message("Done: ", ct, " | genes tested: ", nrow(fcHurdle))
  }
}

# --------------------
# Run both comparisons
# --------------------
dir_create(OUT_LOW_INT)
dir_create(OUT_INT_HIGH)

# LOW vs INT  (reference = "int", test = "low")
run_comparison(
  h5ad_path = H5AD_LOW_INT,
  out_dir   = OUT_LOW_INT,
  clusters  = CLUSTERS,
  ref_level = "low",
  test_level= "int"
)

# INT vs HIGH (reference = "high", test = "int")
run_comparison(
  h5ad_path = H5AD_INT_HIGH,
  out_dir   = OUT_INT_HIGH,
  clusters  = CLUSTERS,
  ref_level = "int",
  test_level= "high"
)

message("\n=== All comparisons finished. ===")


# ---- cell 2 ----
# =====================================================================
# Bootstrap MAST mixed-model DE across cell types & contrasts
#   - Works for LOW vs INT and INT vs HIGH using the same per-CT RDS
#   - Robust to missing covariates (Age/Sex/RIN/total_counts/subject)
# =====================================================================

suppressPackageStartupMessages({
  library(Matrix)
  library(dplyr)
  library(MAST)
  library(lme4)
  library(SingleCellExperiment)
  library(data.table)
})

# -----------------------------
# CONFIG (edit to your project)
# -----------------------------
RDS_DIR         <- "path/files"        # folder with <celltype>.rds (SCE per cell type)
OUT_LOW_INT     <- "path/low_int/"     # output dir for LOW vs INT
OUT_INT_HIGH    <- "path/int_high/"    # output dir for INT vs HIGH
GROUP_COL       <- "Disease.Group"     # colData column with group labels
ITERATIONS      <- 100                 # bootstrap iterations
FRAC_TO_KEEP    <- 0.5                 # fraction of cells per group per iteration
MIN_GENES_KEEP  <- 10                  # safety: min #genes after filtering
FREQ_EXPRESSED  <- 0.15                # genes must be expressed in >=15% cells
MIN_CELLS_GROUP <- 10                  # safety: skip if either group has <10 cells

# Cell types to run
CLUSTERS <- c(
  "Astrocyte-GFAP-OSMR","Astrocyte-SLC1A2-WIF1","Astrocyte-SLC1A2-SMTN","Astrocyte-GFAP-VCAN","OPC",
  "Microglia-Reactive-CD163","Microglia-Homeostatic-CX3CR1","Oligodendrocyte-OPALIN",
  "Ex8:[RORB-TLL1-TMTC4]","Ex9:[RORB-TLL1-PCP4-MID1]","Ex16:[FEZF2-SYT6]","Ex13:[THEMIS-POSTN]",
  "Ex10:[RORB-TLL1-PCP4-TYR]","Ex14:|FEZF2-HTR2C]","Ex3:[CUX2-RORB-GLIS3-SV2C]","Ex15:[FEZF2-ADRA1A]",
  "Ex1:[CUX2-SERPINE2-LAMP5]","Ex2:[CUX2-RORB-GLIS3-LRRC2]","Ex18:[FEZF2-ZFHX3-SCUBE1]","Ex17:[FEZF2-ZFHX3-SEMA3D]",
  "Ex7:[RORB-GABRG1]","Ex4:[CUX2-RORB-COL5A2-CLMN]","Ex5:[RORB-CUX2-EYA4]","Ex12:[THEMIS-PRRX1]",
  "Ex6:[RORB-MME]","Ex11:[RORB-ADGRL4]","In2:[LHX6-PVALB-MEPE]","In17:[ADARB2-VIP-ABI3BP]",
  "In7:[LHX6-SST-B3GAT2]","In1:[LHX6-PVALB-CLMN]","In3:[LHX6-PVALB-COL15A1]","In6:[LHX6-SST-SLC9A2]",
  "In15:[ADARB2-VIP-DACH2]","In16:[ADARB2-VIP-TAC3-NRP1]","In14:[ADARB2-SEMA3C]","In19:[ADARB2-CALB2-SCML4]",
  "In18:[ADARB2-VIP-EXPH5]","In11:[ADARB2-LAMP5-KIT]","In4:[LHX6-SST-MSR1]","In9:[LHX6-SST-NPY]",
  "In5:[LHX6-SST-SPON1]","In8:[LHX6-SST-SEL1L3]","In12:[ADARB2-LAMP5-NDNF]","In13:[ADARB2-SYT6]",
  "In10:[LHX6-ADARB2-LAMP5-HCRTR2]"
)

# -----------------------------------
# Utility helpers (path/dirs, formula)
# -----------------------------------
dir_create <- function(p) if (!dir.exists(p)) dir.create(p, recursive = TRUE, showWarnings = FALSE)
sanitize_tag <- function(x) gsub("[^A-Za-z0-9._-]+", "_", x)

build_formula <- function(sca) {
  # Always include test and cngeneson; add covariates if present with variance
  terms <- c("test")
  # Random intercept by subject if available with >1 level
  if ("subject" %in% colnames(colData(sca)) && length(unique(na.omit(colData(sca)$subject))) > 1) {
    terms <- c(terms, "(1 | subject)")
  }
  # Continuous covariates
  add_if_ok <- function(v) {
    if (v %in% colnames(colData(sca))) {
      u <- unique(na.omit(colData(sca)[[v]]))
      if (length(u) > 1) return(v)
    }
    return(NULL)
  }
  conts <- c("cngeneson", "Age", "RIN", "total_counts")
  cats  <- c("Sex")
  for (v in conts) {
    vv <- add_if_ok(v)
    if (!is.null(vv)) terms <- c(terms, vv)
  }
  # Categorical Sex (only if >1 level)
  if ("Sex" %in% colnames(colData(sca)) && length(unique(na.omit(colData(sca)$Sex))) > 1) {
    terms <- c(terms, "Sex")
  }
  as.formula(paste("~", paste(terms, collapse = " + ")))
}

prep_sca <- function(sce) {
  # counts + logcounts
  if (!"counts" %in% assayNames(sce)) {
    # fall back to first assay if counts missing
    assayNames(sce)[1] <- "counts"
  }
  if (is.null(counts(sce))) {
    counts(sce) <- assay(sce, "counts")
  }
  logcounts(sce) <- log2(counts(sce) + 1)

  sca <- SceToSingleCellAssay(sce)

  # CDR
  cdr <- colSums(assay(sca) > 0)
  colData(sca)$cngeneson <- scale(cdr)

  #  thresholding 
  thres <- thresholdSCRNACountMatrix(assay(sca), cutbins = NULL, nbins = 10,
                                     min_per_bin = 30, bin_by = "median")
  assays(sca, withDimnames = FALSE) <- list(thresh = thres$counts_threshold, tpm = assay(sca))

  # Filter genes by expression frequency
  keep <- freq(sca) > FREQ_EXPRESSED
  if (sum(keep) < MIN_GENES_KEEP) return(NULL)
  sca[keep, ]
}

bootstrap_contrast <- function(sce_full, ref_level, test_level, out_dir, tag, iterations = ITERATIONS, frac = FRAC_TO_KEEP) {
  message("    Contrast: ", toupper(test_level), " vs ", toupper(ref_level))
  dir_create(out_dir)

  # split by group (lowercase)
  g <- tolower(as.character(colData(sce_full)[[GROUP_COL]]))
  if (!all(c(ref_level, test_level) %in% unique(g))) {
    warning("    Missing groups in data for ", tag, " (have: ", paste(sort(unique(g)), collapse = ", "),
            "; need: ", ref_level, ", ", test_level, "). Skipping.")
    return(invisible(NULL))
  }
  inter <- sce_full[, g == ref_level]   # reference group cells
  test  <- sce_full[, g == test_level]  # test group cells

  n_ref  <- ncol(inter); n_test <- ncol(test)
  if (n_ref < MIN_CELLS_GROUP || n_test < MIN_CELLS_GROUP) {
    warning("    Too few cells (ref=", n_ref, ", test=", n_test, ") in ", tag, ". Skipping.")
    return(invisible(NULL))
  }

  keep_ref  <- max(1, floor(n_ref  * frac))
  keep_test <- max(1, floor(n_test * frac))

  iter_output <- vector("list", iterations)

  for (i in seq_len(iterations)) {
    # sample w/o replacement
    sce_ref  <- inter[, sample(colnames(inter), keep_ref)]
    sce_test <- test[,  sample(colnames(test),  keep_test)]
    sce_merged <- cbind(sce_ref, sce_test)

    sca <- prep_sca(sce_merged)
    if (is.null(sca)) {
      warning("    Iter ", i, ": < ", MIN_GENES_KEEP, " genes after filtering. Skipping iter.")
      next
    }

    # group factor
    giter <- factor(tolower(as.character(colData(sca)[[GROUP_COL]])))
    giter <- stats::relevel(giter, ref = ref_level)
    colData(sca)$test <- giter
    contrast_name <- paste0("test", test_level)

    # model
    form <- build_formula(sca)
    zfit <- tryCatch(
      zlm(form, sca, method = "glmer", ebayes = FALSE),
      error = function(e) { warning("    Iter ", i, ": zlm failed: ", conditionMessage(e)); return(NULL) }
    )
    if (is.null(zfit)) next

    # logFC table
    FC <- tryCatch(getLogFC(zfit), error = function(e) NULL)
    if (is.null(FC)) {
      warning("    Iter ", i, ": getLogFC failed.")
      next
    }
    FC <- as.data.table(FC)
    FC <- FC[contrast == contrast_name, .(primerid, logFC)]

    # LRT
    sm <- tryCatch(summary(zfit, doLRT = contrast_name), error = function(e) NULL)
    if (is.null(sm)) {
      warning("    Iter ", i, ": summary(doLRT) failed.")
      next
    }
    dt <- as.data.table(sm$datatable)

    # Merge hurdle p and continuous coef/CI
    de <- merge(
      dt[contrast == contrast_name & component == "H",    .(primerid, `Pr(>Chisq)`)],
      dt[contrast == contrast_name & component == "logFC",.(primerid, coef, ci.hi, ci.lo)],
      by = "primerid"
    )
    if (!nrow(de)) next

    de[, fdr := p.adjust(`Pr(>Chisq)`, method = "fdr")]
    de <- merge(de, FC, by = "primerid", all.x = TRUE)  # add logFC (from getLogFC)

    iter_output[[i]] <- de
    if (i %% 10 == 0) message("      Iter ", i, "/", iterations)
  }

  # keep only iterations with results
  iter_output <- Filter(Negate(is.null), iter_output)
  if (!length(iter_output)) {
    warning("    No successful iterations for ", tag, ".")
    return(invisible(NULL))
  }

  # filter FDR < 0.05 per iteration
  result <- lapply(iter_output, function(x) x[fdr < 0.05])

  # assemble matrices
  n_iter <- length(result)
  gene_list <- unique(unlist(lapply(result, function(x) x$primerid)))
  if (!length(gene_list)) {
    warning("    No DE genes at FDR<0.05 across iterations for ", tag, ".")
    return(invisible(NULL))
  }

  mat_logFC <- matrix(NA_real_, nrow = length(gene_list), ncol = n_iter,
                      dimnames = list(gene_list, paste0("iter", seq_len(n_iter))))
  mat_q     <- matrix(NA_real_, nrow = length(gene_list), ncol = n_iter,
                      dimnames = list(gene_list, paste0("iter", seq_len(n_iter))))

  for (k in seq_len(n_iter)) {
    if (!nrow(result[[k]])) next
    rk <- result[[k]][, .(primerid, logFC, fdr)]
    mat_logFC[rk$primerid, k] <- rk$logFC
    mat_q[rk$primerid, k]     <- rk$fdr
  }

  df_logFC <- as.data.frame(mat_logFC)
  df_q     <- as.data.frame(mat_q)
  df_logFC$mean_logFC <- apply(df_logFC, 1, function(x) mean(x, na.rm = TRUE))
  df_q$mean_qvalue    <- apply(df_q, 1, function(x) mean(x, na.rm = TRUE))

  # write
  tag_safe <- sanitize_tag(tag)
  write.csv(df_logFC, file.path(out_dir, paste0(ref_level, "_", test_level, "_", tag_safe, "_logFC_iteration.csv")))
  write.csv(df_q,     file.path(out_dir, paste0(ref_level, "_", test_level, "_", tag_safe, "_qvalue_iteration.csv")))
  invisible(NULL)
}

# -----------------------------
# run both contrasts
# -----------------------------
dir_create(OUT_LOW_INT)
dir_create(OUT_INT_HIGH)

for (ct in CLUSTERS) {
  message("\n=== Cell type: ", ct, " ===")
  rds_path <- file.path(RDS_DIR, paste0(ct, ".rds"))
  if (!file.exists(rds_path)) {
    warning("  Missing RDS for ", ct, " at ", rds_path, ". Skipping.")
    next
  }
  sce <- readRDS(rds_path)

  # Ensure GROUP_COL exists
  if (!(GROUP_COL %in% colnames(colData(sce)))) {
    warning("  '", GROUP_COL, "' not found in colData for ", ct, ". Skipping.")
    next
  }

  # LOW vs INT  (ref = int, test = low)
  bootstrap_contrast(
    sce_full  = sce,
    ref_level = "low",
    test_level= "int",
    out_dir   = OUT_LOW_INT,
    tag       = ct
  )

  # INT vs HIGH (ref = high, test = int)
  bootstrap_contrast(
    sce_full  = sce,
    ref_level = "int",
    test_level= "high",
    out_dir   = OUT_INT_HIGH,
    tag       = ct
  )
}

message("\nAll bootstrap analyses completed.")


# ---- cell 3 ----



import argparse
import os
from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
import scanpy as sc
from anndata import AnnData

from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats
from pydeseq2.utils import test_valid_counts

# -----------------------------
# Defaults / constants
# -----------------------------
CELLTYPES_DEFAULT: List[str] = [
    "Astrocyte-GFAP-OSMR","Astrocyte-GFAP-VCAN","Astrocyte-SLC1A2-SMTN","Astrocyte-SLC1A2-WIF1",
    "Ex1:[CUX2-SERPINE2-LAMP5]","Ex2:[CUX2-RORB-GLIS3-LRRC2]","Ex3:[CUX2-RORB-GLIS3-SV2C]",
    "Ex4:[CUX2-RORB-COL5A2-CLMN]","Ex5:[RORB-CUX2-EYA4]","Ex6:[RORB-MME]","Ex7:[RORB-GABRG1]",
    "Ex8:[RORB-TLL1-TMTC4]","Ex9:[RORB-TLL1-PCP4-MID1]","Ex10:[RORB-TLL1-PCP4-TYR]","Ex11:[RORB-ADGRL4]",
    "Ex12:[THEMIS-PRRX1]","Ex13:[THEMIS-POSTN]","Ex14:|FEZF2-HTR2C]","Ex15:[FEZF2-ADRA1A]","Ex16:[FEZF2-SYT6]",
    "Ex17:[FEZF2-ZFHX3-SEMA3D]","Ex18:[FEZF2-ZFHX3-SCUBE1]","In1:[LHX6-PVALB-CLMN]","In2:[LHX6-PVALB-MEPE]",
    "In3:[LHX6-PVALB-COL15A1]","In4:[LHX6-SST-MSR1]","In5:[LHX6-SST-SPON1]","In6:[LHX6-SST-SLC9A2]",
    "In7:[LHX6-SST-B3GAT2]","In8:[LHX6-SST-SEL1L3]","In9:[LHX6-SST-NPY]","In10:[LHX6-ADARB2-LAMP5-HCRTR2]",
    "In11:[ADARB2-LAMP5-KIT]","In12:[ADARB2-LAMP5-NDNF]","In13:[ADARB2-SYT6]","In14:[ADARB2-SEMA3C]",
    "In15:[ADARB2-VIP-DACH2]","In16:[ADARB2-VIP-TAC3-NRP1]","In17:[ADARB2-VIP-ABI3BP]","In18:[ADARB2-VIP-EXPH5]",
    "In19:[ADARB2-CALB2-SCML4]","Microglia-Homeostatic-CX3CR1","Microglia-Reactive-AIF1",
    "Microglia-Reactive-CACNA1B","Microglia-Reactive-CD163","OPC","Oligodendrocyte-COL18A1",
    "Oligodendrocyte-OPALIN","Pericytes","VLMC","endothelial"
]

BRAIN_REGION_COL = "Brain.Region"
GROUP_COL = "Disease.Group"
SUBJECT_COL = "subject"
AUTHOR_CT_COL = "Author_Annotation"

# Gene filtering for DESeq input
MIN_SAMPLES_PER_GENE = 2     # keep genes expressed (>0) in at least this many samples
MIN_COUNTS_PER_GENE = 10     # and total counts across samples >= this

# Require at least N pseudobulk samples per group to run DE
MIN_PB_SAMPLES_PER_GROUP = 2

# -----------------------------
# Helpers
# -----------------------------
def sanitize(s: str) -> str:
    return "".join(ch if ch.isalnum() or ch in "._-[]" else "_" for ch in s)

def pick_counts_layer(adata: AnnData) -> Optional[str]:
    """Pick a sensible counts source. Preference: layers['counts'] -> layers['unspliced'] -> X."""
    if "counts" in adata.layers:
        return "counts"
    if "unspliced" in adata.layers:
        return "unspliced"
    return None  # use X

def to_int_counts(mat) -> np.ndarray:
    """Ensure integer counts (DESeq2 requirement)."""
    try:
        import scipy.sparse as sp
        if sp.issparse(mat):
            # Sum operations later will densify row-wise anyway for small PB; if huge, adapt.
            mat = mat.A
    except Exception:
        pass
    if not np.issubdtype(mat.dtype, np.integer):
        mat = np.rint(mat).astype(np.int64)
    mat[mat < 0] = 0
    return mat

def pseudobulk_by_subject(adata: AnnData, counts_layer: Optional[str]) -> AnnData:
    """Sum counts per subject to produce pseudobulk samples."""
    X = adata.layers[counts_layer] if counts_layer is not None else adata.X
    X = to_int_counts(X)

    # Sum by subject
    subjects = adata.obs[SUBJECT_COL].astype(str).values
    df = pd.DataFrame(X, columns=adata.var_names)
    df["__subject__"] = subjects
    summed = df.groupby("__subject__", sort=False).sum()
    counts = summed.drop(columns="__subject__", errors="ignore") if "__subject__" in summed.columns else summed

    # Clinical / metadata (just Disease.Group for design)
    clin = (
        adata.obs[[SUBJECT_COL, GROUP_COL]]
        .drop_duplicates(subset=[SUBJECT_COL])
        .set_index(SUBJECT_COL)
        .loc[counts.index]  # align to counts
        .copy()
    )
    clin[GROUP_COL] = clin[GROUP_COL].astype(str).str.lower()

    # Quick validity
    test_valid_counts(counts)

    pb = sc.AnnData(X=counts.values)
    pb.var_names = counts.columns
    pb.obs_names = counts.index.astype(str)
    pb.obs[GROUP_COL] = clin[GROUP_COL].values
    return pb

def filter_genes_for_deseq(counts: pd.DataFrame) -> pd.DataFrame:
    """Filter genes by prevalence and counts."""
    is_expressed = (counts > 0).sum(axis=0) >= MIN_SAMPLES_PER_GENE
    enough_counts = counts.sum(axis=0) >= MIN_COUNTS_PER_GENE
    keep = is_expressed & enough_counts
    return counts.loc[:, keep]

def run_contrast_for_ct(
    early: AnnData,
    celltype: str,
    contrast: Tuple[str, str],  # (numerator, denominator) e.g., ("low","int")
    out_dir: str
) -> Optional[str]:
    """Run one contrast for one cell type. Returns path to CSV (or None)."""
    num, den = contrast  # log2FC ~ num/den
    ct_mask = early.obs[AUTHOR_CT_COL] == celltype
    if ct_mask.sum() == 0:
        print(f"[skip] {celltype}: no cells")
        return None

    ad = early[ct_mask].copy()
    # Need both groups present
    groups = ad.obs[GROUP_COL].astype(str).str.lower().unique().tolist()
    if not set([num, den]).issubset(set(groups)):
        print(f"[skip] {celltype} ({num}_vs_{den}): missing groups (have: {groups})")
        return None

    # Need subject column
    if SUBJECT_COL not in ad.obs.columns:
        print(f"[skip] {celltype}: '{SUBJECT_COL}' not in .obs")
        return None

    counts_layer = pick_counts_layer(ad)
    pb = pseudobulk_by_subject(ad, counts_layer=counts_layer)

    # Keep only samples in num/den
    pb = pb[pb.obs[GROUP_COL].isin([num, den])].copy()
    grp_counts = pb.obs[GROUP_COL].value_counts().to_dict()
    if grp_counts.get(num, 0) < MIN_PB_SAMPLES_PER_GROUP or grp_counts.get(den, 0) < MIN_PB_SAMPLES_PER_GROUP:
        print(f"[skip] {celltype} ({num}_vs_{den}): need ≥{MIN_PB_SAMPLES_PER_GROUP} samples per group; have {grp_counts}")
        return None

    counts = pd.DataFrame(pb.X, index=pb.obs_names, columns=pb.var_names)
    counts = filter_genes_for_deseq(counts)
    if counts.shape[1] == 0:
        print(f"[skip] {celltype} ({num}_vs_{den}): no genes after filtering")
        return None

    clinical = pb.obs[[GROUP_COL]].copy()
    clinical[GROUP_COL] = clinical[GROUP_COL].astype("category")

    # Fit DESeq2 and run contrast
    dds = DeseqDataSet(counts=counts, clinical=clinical, design_factors=GROUP_COL)
    dds.deseq2()

    stats = DeseqStats(dds, contrast=(GROUP_COL, num, den), alpha=0.05)  # log2FC num/den
    stats.summary()
    res = stats.results_df.copy()
    res["gene"] = res.index
    res["upregulated_in"] = np.where(res["log2FoldChange"] > 0, num, den)
    res = res.sort_values(["padj", "stat"], ascending=[True, False])

    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{sanitize(celltype)}_pseudobulk_{num}_vs_{den}.csv")
    res.to_csv(out_path, index=False)
    print(f"[done] {celltype} ({num}_vs_{den}): {out_path}")
    return out_path

# -----------------------------
# Main
# -----------------------------
def main():
    ap = argparse.ArgumentParser(description="Pseudobulk DE for LOW vs INT and INT vs HIGH per cell type.")
    ap.add_argument("--h5ad", required=True, help="Path to input .h5ad")
    ap.add_argument("--outdir", required=True, help="Output directory")
    ap.add_argument("--region", default="Frontal Cx (BA9)", help="Region label to keep (Brain.Region)")
    ap.add_argument("--celltypes", nargs="*", default=CELLTYPES_DEFAULT, help="Cell types to analyze")
    args = ap.parse_args()

    adata = sc.read_h5ad(args.h5ad)

    # Filter to region
    if BRAIN_REGION_COL not in adata.obs.columns:
        raise ValueError(f"'{BRAIN_REGION_COL}' not found in .obs")
    adata = adata[adata.obs[BRAIN_REGION_COL].isin([args.region])].copy()

    # Normalize group labels
    if GROUP_COL not in adata.obs.columns:
        raise ValueError(f"'{GROUP_COL}' not found in .obs")
    adata.obs[GROUP_COL] = adata.obs[GROUP_COL].astype(str).str.lower()

    # Keep only groups in any of {low,int,high} to reduce memory
    keep_groups = ["low", "int", "high"]
    adata = adata[adata.obs[GROUP_COL].isin(keep_groups)].copy()
    if adata.n_obs == 0:
        raise ValueError(f"No cells remain after filtering to {args.region} and Disease.Group in {keep_groups}.")

    # Early and Late subsets for convenience
    early = adata[adata.obs[GROUP_COL].isin(["low", "int"])].copy()
    late  = adata[adata.obs[GROUP_COL].isin(["int", "high"])].copy()

    out_low_int  = os.path.join(args.outdir, "low_vs_int")
    out_int_high = os.path.join(args.outdir, "int_vs_high")

    done = []

    for ct in args.celltypes:
        try:
            # LOW vs INT
            out1 = run_contrast_for_ct(early, ct, contrast=("int", "low"), out_dir=out_low_int)
            if out1: done.append(out1)
            # INT vs HIGH
            out2 = run_contrast_for_ct(late, ct, contrast=("high", "int"), out_dir=out_int_high)
            if out2: done.append(out2)
        except Exception as e:
            print(f"[error] {ct}: {e}")

    print(f"\nCompleted. Wrote {len(done)} files under: {args.outdir}")


if __name__ == "__main__":
    main()


### Helper function

python pseudobulk_deseq_dual_contrasts.py \
  --h5ad path/dataset.h5ad \
  --outdir results/pseudobulk_dual \
  --region "Frontal Cx (BA9)"


