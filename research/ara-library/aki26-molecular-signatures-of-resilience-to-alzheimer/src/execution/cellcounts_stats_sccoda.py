# Grounding: transcribed
# Source: cellcounts_stats_methods_scCODA.ipynb (author repo AkilaRanjith/Molecular-Signatures-of-Resilience...); code cells only (outputs stripped).

# ---- cell 1 ----
import numpy as np
import pandas as pd
import scanpy as sc
import anndata 

### read the anndata after celltype annotation

bdata=sc.read_h5ad("path/dataset.h5ad")

#### subset the data for neuronal population

Neuron=bdata[bdata.obs['major_celltypes'].isin(["Excitatory","Inhibitory"])]


#### subset the data based on Brain Region

BA9=Neuron[Neuron.obs["Brain.Region"] == "Frontal Cx (BA9)"]
BA7=Neuron[Neuron.obs["Brain.Region"] == "Precuneous (BA7)"]
BA17=Neuron[Neuron.obs["Brain.Region"] == "Primary Visual Cx (BA17)"]


#### plot the proportion for each brain region

# count the number of occurrences  for each cluster ID
count = BA9.obs.groupby(['Disease.Group', 'Author_Annotation']).size()
new_df = count.to_frame(name = 'size').reset_index()

# Pivot and rename columns
freq = new_df.pivot(index='Disease.Group', columns='Author_Annotation')['size']
list2 = ["Ex1", "Ex2", "Ex3", "Ex4", "Ex5", "Ex6", "Ex7", "Ex8", "Ex9", "Ex10", "Ex11", "Ex12", "Ex13", "Ex14", "Ex15", "Ex16", "Ex17", "Ex18", 
         "In1", "In2", "In3", "In4", "In5", "In6", "In7", "In8", "In9", "In10", "In11", "In12", "In13", "In14", "In15", "In16", "In17", "In18", "In19"]
freq.columns = list2

# Normalize
percent = freq.div(freq.sum(axis=1), axis=0).T
percent['Clusters'] = percent.index

# Select Disease.Groups
T_new = percent[['low', 'int', 'high', 'Clusters']]

# Standard error 
se_new = T_new[['low', 'int', 'high']].apply(lambda col: np.std(col, ddof=1) / np.sqrt(len(col)), axis=0)

# Plot 
plt.rcParams.update({'font.size': 28})
T_new.plot(x='Clusters', kind='bar', figsize=(30, 7), width=0.8, color=['cyan', 'blue', 'red'], 
           edgecolor='black', capsize=2, title='Proportion of Neuronal Cell Types in BA9')
plt.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=5)
plt.ylabel("Cell Proportion", fontsize=22)

# Error bars
x_positions = np.arange(len(T_new['Clusters']))
for i, col in enumerate(['low', 'int', 'high']):
    plt.errorbar(x_positions + i * 0.3 - 0.3, T_new[col], yerr=se_new[i], fmt='none', color='black', capsize=3)

plt.show()


# ---- cell 2 ----
import scanpy as sc
import numpy as np
import pandas as pd

# List unique layer annotation specified in the anndata
unique_cell_types = BA9_AllNuc_neurons.obs['layers1'].unique()

# List to store rows before creating DataFrame
rows = []

# Calculate cell proportions per subject per cell type
for cell_type in unique_cell_types:
    cell_data = BA9_AllNuc_neurons[BA9_AllNuc_neurons.obs['layers1'] == cell_type].obs
    total_cells = len(cell_data)
    
    grouped = cell_data.groupby(['Donor', 'Disease.Group', 'Assay', 'APOE_class', 'Age', 'Sex'])
    
    for group_keys, group_df in grouped:
        subject, disease_group, assay, apoe_class, age, sex = group_keys
        proportion = len(group_df) / total_cells
        rows.append({
            'CellType': cell_type,
            'Subject': subject,
            'Assay': assay,
            'Disease_Group': disease_group,
            'APOE_class': apoe_class,
            'Age': age,
            'Sex': sex,
            'Proportion': proportion
        })

# Convert to DataFrame
cell_proportions_df = pd.DataFrame(rows)
cell_proportions_df.to_csv("path/BA9_AllNuc_neurons_proportions.csv")

# ---- cell 3 ----

# Load Required Libraries

library(dplyr)
library(tidyr)


# Step 1: Load and Prepare Data : Input-Proportion data 

data <- read.csv("path/BA9_AllNuc_neurons_proportions.csv")


### adjust age treat them as covraiate
data <- data %>%
  mutate(
    Age = case_when(Age == "95 and above" ~ "95", TRUE ~ Age),
    Age = as.numeric(Age),
    Disease_Group = factor(Disease_Group, levels = c("low", "int", "high")),
    Assay = factor(Assay),
    APOE_class = factor(APOE_class),
    Sex = factor(Sex),
    Proportion = pmin(pmax(Proportion, 1e-5), 1 - 1e-5)
  ) %>%
  filter(!is.na(Age), !is.na(APOE_class), !is.na(Proportion))


# Step 2: Fit Unweighted Beta GLMM per Cell Type

celltypes <- unique(data$CellType)
results <- list()

for (ct in celltypes) {
  message("Processing: ", ct)
  subdata <- data %>% filter(CellType == ct) %>% droplevels()
  
  if (n_distinct(subdata$Subject) < 3) next
  
  model <- tryCatch({
    glmmTMB(
      Proportion ~ Disease_Group + Assay + Age + APOE_class + Sex + (1 | Subject),
      family = beta_family(link = "logit"),
      data = subdata
    )
  }, error = function(e) {
    warning("Model failed for ", ct, ": ", e$message)
    return(NULL)
  })
  ### dipsly error message


  ### model outputs
  
  if (!is.null(model)) {
    coef_summary <- summary(model)$coefficients$cond
    result_df <- data.frame(
      CellType = ct,
      Coefficient = rownames(coef_summary),
      Estimate = coef_summary[, "Estimate"],
      StdError = coef_summary[, "Std. Error"],
      z_value = coef_summary[, "z value"],
      p_value = coef_summary[, "Pr(>|z|)"],
      stringsAsFactors = FALSE
    )
    results[[ct]] <- result_df
  }
}


# Step 3: Apply FDR Correction


combined_results <- bind_rows(results) %>%
  mutate(FDR = p.adjust(p_value, method = "BH"))


# Step 4: Save Results

write.csv(combined_results,
          "path/results/BA9_AllNuc_neurons_proportions_LMM_results.csv",
          row.names = FALSE)

message(" Unweighted Beta GLMM complete. Results saved.")


# ---- cell 4 ----
import matplotlib.pyplot as plt
import numpy as np

### read the dataframe for plotting
BA9=pd.read_csv("/path BA9.csv")

# Sample DataFrame columns
Y = BA9['log10_pvalue']
X = BA9['z_value']
labels = BA9['CellType']
p_value = BA9['p_value']
log_p_values = -np.log10(p_value)

significance_threshold = -np.log10(0.07)

plt.figure(figsize=(12, 10))

# Get unique cell types and assign a distinct color to each
unique_celltypes = np.unique(labels)
cmap = plt.get_cmap("tab20")
color_dict = {celltype: cmap(i % 20) for i, celltype in enumerate(unique_celltypes)}

# Plot and annotate non-significant points
for celltype in unique_celltypes:
    idx = (labels == celltype) & (log_p_values < significance_threshold)
    plt.scatter(
        X[idx], log_p_values[idx], marker='o', s=90,
        c=[color_dict[celltype]], edgecolor="black", label=celltype
    )

    # Annotate each non-significant point
    for i in np.where(idx)[0]:
        x_pos = X[i] + 0.05
        y_pos = log_p_values[i]
        plt.annotate(
            labels[i], (x_pos, y_pos),
            fontsize=12, alpha=0.6,
            textcoords='offset points', xytext=(5, 0)
        )

# Plot and annotate significant points in red
for i in range(len(X)):
    if log_p_values[i] >= significance_threshold:
        plt.scatter(
            X[i], log_p_values[i],
            marker='s', s=100, color='red', edgecolor="black"
        )
        x_pos = X[i] + 0.05
        y_pos = log_p_values[i]
        plt.annotate(
            labels[i], (x_pos, y_pos),
            fontsize=12, fontweight='bold',
            textcoords='offset points', xytext=(5, 0)
        )

# Plot formatting
plt.rcParams.update({'font.size': 14})
plt.xlabel("Z scores")
plt.ylabel("-log10(p-value)")
plt.xlim(-3.5, 3.5)
plt.grid(True, linestyle='--', alpha=0.7, color='black')

# Legend for cell types
plt.legend(title="Cell Type", bbox_to_anchor=(1.05, 1), loc='upper left')

# Save plot
plt.tight_layout()
plt.savefig("path/BA9_LMM_plot_all.pdf", format='pdf')
plt.show()



# ---- cell 5 ----
#!/usr/bin/env python3
"""
scCODA compositional analysis on BA9 subset

"""

import argparse
import os
import shutil
from pathlib import Path

import numpy as np
import pandas as pd
import scanpy as sc
from sklearn.impute import SimpleImputer

# scCODA
from sccoda.util import comp_ana as mod
from sccoda.util import cell_composition_data as dat

# Viz
import seaborn as sns
import matplotlib.pyplot as plt


def empty_dir(path: str):
    """Delete contents of a directory without removing the directory."""
    Path(path).mkdir(parents=True, exist_ok=True)
    for name in os.listdir(path):
        p = os.path.join(path, name)
        try:
            if os.path.isfile(p) or os.path.islink(p):
                os.remove(p)
            elif os.path.isdir(p):
                shutil.rmtree(p)
        except Exception as e:
            print(f"Failed to delete {p}: {e}")


def coerce_numeric(series: pd.Series, replace_values=("95 or above",)) -> pd.Series:
    s = series.copy()
    for v in replace_values:
        s = s.replace(v, np.nan)
    s = pd.to_numeric(s, errors="coerce")
    return s


def zscore(series: pd.Series) -> pd.Series:
    return (series - series.mean()) / series.std(ddof=0)


def main():
    ap = argparse.ArgumentParser(description="scCODA compositional analysis for BA9.")
    ap.add_argument("--h5ad", required=True, help="Path to adata.h5ad")
    ap.add_argument("--rootdir", default=".", help="Root directory (for relative paths)")
    ap.add_argument("--outdir", default="results/BA9_AllNuc_NeuN", help="Output directory")
    ap.add_argument("--region", default="Frontal Cx (BA9)", help="Brain region value to keep")
    ap.add_argument("--thresholds", nargs="*", type=int, default=[500], help="n_genes lower thresholds")
    ap.add_argument("--disease_col", default="Disease.Group", help="Column with disease group")
    ap.add_argument("--celltype_col", default="layers1", help="Column with cell-type labels")
    ap.add_argument("--group_order", nargs="*", default=["low", "int", "high"], help="Disease group order")
    ap.add_argument("--assay_ref", default="DropSeq", help="Reference level for Assay")
    ap.add_argument("--sex_ref", default="F", help="Reference level for Sex")
    ap.add_argument("--apoe_ref", default="E3/E3", help="Reference level for APOE_class")
    ap.add_argument("--empty_outdir", action="store_true", help="Empty output dir before writing")
    ap.add_argument("--neurons_list", nargs="*", default=None,
                    help="Explicit list of neuron cell types to plot. "
                         "If not provided, any cell type starting with 'Ex' will be used.")
    args = ap.parse_args()

    out_dir = os.path.join(args.rootdir, args.outdir)
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    if args.empty_outdir:
        empty_dir(out_dir)

    # Load and subset to BA9
    adata = sc.read_h5ad(os.path.join(args.rootdir, args.h5ad))
    if "Brain.Region" not in adata.obs.columns:
        raise ValueError("Brain.Region column not found in .obs")
    adata = adata[adata.obs["Brain.Region"].isin([args.region])].copy()

    # Prepare covariates
    if args.disease_col not in adata.obs.columns:
        raise ValueError(f"{args.disease_col} not found in .obs")
    adata.obs["Disease"] = adata.obs[args.disease_col].astype(str)

    sample_variable = "Donor" if "Donor" in adata.obs.columns else ("subject" if "subject" in adata.obs.columns else None)
    if sample_variable is None:
        raise ValueError("Neither 'Donor' nor 'subject' found in .obs")

    if "Age" in adata.obs.columns:
        adata.obs["Age"] = coerce_numeric(adata.obs["Age"])
    else:
        adata.obs["Age"] = np.nan

    num_cols = adata.obs.select_dtypes(include=[np.number]).columns
    if len(num_cols):
        imputer_num = SimpleImputer(strategy="mean")
        adata.obs[num_cols] = imputer_num.fit_transform(adata.obs[num_cols])

    adata.obs["Age_z"] = zscore(adata.obs["Age"])

    if "APOE_class" in adata.obs.columns:
        adata.obs["APOE_class"] = adata.obs["APOE_class"].astype(str).replace("nan", np.nan)
    else:
        adata.obs["APOE_class"] = np.nan

    cat_cols = adata.obs.select_dtypes(include=["category", "object"]).columns
    if len(cat_cols):
        imputer_cat = SimpleImputer(strategy="most_frequent")
        adata.obs[cat_cols] = imputer_cat.fit_transform(adata.obs[cat_cols])

    if "n_genes" not in adata.obs.columns:
        raise ValueError("'n_genes' not found in .obs (needed for threshold filtering)")
    adata.obs["n_genes"] = adata.obs["n_genes"].astype(int)

    # Iterate thresholds n_genes threshold
    for thr in args.thresholds:
        print(f"\n=== n_genes > {thr} ===")
        ad_thr = adata[adata.obs["n_genes"] > thr].copy()
        if ad_thr.n_obs == 0:
            print("No cells remain after threshold; skipping.")
            continue

        if args.celltype_col not in ad_thr.obs.columns:
            raise ValueError(f"{args.celltype_col} not found in .obs")

        df_obs = ad_thr.obs.copy()

        # Counts per donor x cell type
        cluster_counts = (
            df_obs.groupby([sample_variable, args.celltype_col]).size().reset_index(name="cell_count")
        )
        cluster_counts_pivot = (
            cluster_counts.pivot(index=sample_variable, columns=args.celltype_col, values="cell_count").fillna(0)
        )
        cluster_counts_pivot = cluster_counts_pivot.astype(int)

        # Proportions per donor
        df_normalized = cluster_counts_pivot.div(cluster_counts_pivot.sum(axis=1), axis=0)
        df_normalized.index.name = sample_variable
        df_normalized = df_normalized.reset_index()

        # Build scCODA data object
        cluster_counts_pivot[sample_variable] = cluster_counts_pivot.index
        data_all = dat.from_pandas(cluster_counts_pivot, covariate_columns=[sample_variable])

        # Donor-level covariates
        sample_obs = df_obs.groupby(sample_variable, as_index=False).first().set_index(sample_variable)
        data_all.obs = sample_obs

        # Ensure Disease is categorical with specified order
        data_all.obs["Disease"] = pd.Categorical(
            data_all.obs["Disease"], categories=args.group_order, ordered=True
        )

        # Save raw proportions by Disease
        merged_prop = pd.merge(
            data_all.obs[["Disease"]], df_normalized.set_index(sample_variable),
            left_index=True, right_index=True, how="inner"
        )
        merged_prop["Donor"] = merged_prop.index
        merged_prop.to_excel(os.path.join(out_dir, f"{thr}_scCoda_Proportions_All.xlsx"))

        # scCODA model
        formula_terms = ["C(Disease, Treatment('low'))"]
        if "Sex" in data_all.obs.columns:
            formula_terms.append(f"C(Sex, Treatment('{args.sex_ref}'))")
        if "APOE_class" in data_all.obs.columns:
            formula_terms.append(f"C(APOE_class, Treatment('{args.apoe_ref}'))")
        if "Assay" in data_all.obs.columns:
            formula_terms.append(f"C(Assay, Treatment('{args.assay_ref}'))")
        if "Age_z" in data_all.obs.columns:
            formula_terms.append("Age_z")
        formula = " + ".join(formula_terms) if formula_terms else "1"

        model = mod.CompositionalAnalysis(
            data_all,
            formula=formula,
            reference_cell_type="automatic"
        )

        sim_results = model.sample_hmc()
        tag = f"BA9_AllNuc_NeuN_{thr}"

        sim_results.save(os.path.join(out_dir, f"{tag}_results.pkl"))
        sim_results.credible_effects().to_excel(os.path.join(out_dir, f"{tag}_credible_effects.xlsx"))
        pd.DataFrame(sim_results.summary()).to_excel(os.path.join(out_dir, f"{tag}_summary.xlsx"))

        full_results = pd.concat(
            [pd.DataFrame(sim_results.credible_effects()), sim_results.effect_df], axis=1
        )
        full_results.to_excel(os.path.join(out_dir, f"{tag}_full_results.xlsx"))

        # Barplot (neuronal types)
        if args.neurons_list is not None and len(args.neurons_list):
            neurons = args.neurons_list
        else:
            neurons = sorted([c for c in cluster_counts_pivot.columns if isinstance(c, str) and c.startswith("Ex")])

        if len(neurons) == 0:
            print("No neuron cell types detected for barplot; skipping plot.")
            continue

        df_norm_long = df_normalized.melt(
            id_vars=[sample_variable],
            var_name=args.celltype_col,
            value_name="Proportion"
        )
        merged_df = pd.merge(df_norm_long, data_all.obs[["Disease"]], left_on=sample_variable, right_index=True)
        merged_df["Disease"] = pd.Categorical(merged_df["Disease"], categories=args.group_order, ordered=True)
        plot_df = merged_df[merged_df[args.celltype_col].isin(neurons)].copy()
        plot_df[args.celltype_col] = plot_df[args.celltype_col].str.replace(r":.*", "", regex=True)

        sns.set(style="whitegrid")
        plt.figure(figsize=(20, 6))
        ax = sns.barplot(
            data=plot_df,
            x=args.celltype_col,
            y="Proportion",
            hue="Disease",
            ci="sd",
            capsize=0.1,
            errwidth=1.2,
            order=sorted(plot_df[args.celltype_col].unique()),
        )
        ax.legend(title="Disease")
        plt.xticks(rotation=90, ha="right", fontsize=10)
        plt.ylabel("Proportion", fontsize=12)
        plt.xlabel(args.celltype_col, fontsize=12)
        plt.title("Proportion of excitatory neuron types by Disease", fontsize=14, fontweight="bold")
        plt.tight_layout()
        plt.savefig(os.path.join(out_dir, f"{tag}_barplot.pdf"), format="pdf", bbox_inches="tight")
        plt.close()

    print(f"\nDone. Outputs in: {out_dir}")


if __name__ == "__main__":
    main()


