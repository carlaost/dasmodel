# Grounding: transcribed
# Source: xenium_segmentation_analysis.ipynb (author repo AkilaRanjith/Molecular-Signatures-of-Resilience...); code cells only (outputs stripped).

# ---- cell 1 ----
import scanpy as sc
import squidpy as sq
import pandas as pd

# ---- cell 2 ----
export PATH=~installedfolder:$PATH
xeniumranger resegment --id=sample_name --xenium-bundle=output_xenium_bundle_path --boundary-stain=disable

# ---- cell 3 ----
###import the slide of interest

import spatialdata_io

# Correctly specify the path as a string
xenium_data_path = "Resegmented folder/outs/"

# Try loading with minimal parameters
sdata = spatialdata_io.xenium(xenium_data_path,aligned_images=False,n_jobs=1,cells_as_circles=True)
print(sdata)

# ---- cell 4 ----
from spatialdata_io import xenium_explorer_selection
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

####Select the each tissue coordinates from xenium explorer and input the coordinate csv file 

# Path to the exported CSV file
path_to_csv = "coordinate_file.csv"

# this shows the selceted tissue region

polygon = list(spatialdata_io.xenium_explorer_selection("path to co-ordinate.csv", return_list=False,))
polygon[0]

from spatialdata import polygon_query
cropped_C1 = polygon_query(
    sdata,
    polygon=polygon[0],
    target_coordinate_system="global",
)
cropped_C1

### get the anndata for selected tisuue section
adata=cropped_C1.tables["table"]
adata.obs[['spatial_x', 'spatial_y']] = adata.obsm['spatial']

### Quality check
sc.pp.calculate_qc_metrics(adata, percent_top=(10, 20, 50, 150), inplace=True)
cprobes = (
    adata.obs["control_probe_counts"].sum() / adata.obs["total_counts"].sum() * 100
)
cwords = (
    adata.obs["control_codeword_counts"].sum() / adata.obs["total_counts"].sum() * 100
)
print(f"Negative DNA probe count % : {cprobes}")
print(f"Negative decoding count % : {cwords}")

#### QC plots
fig, axs = plt.subplots(1, 4, figsize=(15, 4))

axs[0].set_title("Total transcripts per cell")
sns.histplot(
    adata.obs["total_counts"],
    kde=False,
    ax=axs[0],
)

axs[1].set_title("Unique transcripts per cell")
sns.histplot(
    adata.obs["n_genes_by_counts"],
    kde=False,
    ax=axs[1],
)


axs[2].set_title("Area of segmented cells")
sns.histplot(
    adata.obs["cell_area"],
    kde=False,
    ax=axs[2],
)

axs[3].set_title("Nucleus ratio")
sns.histplot(
    adata.obs["nucleus_area"] / adata.obs["cell_area"],
    kde=False,
    ax=axs[3],
)

### Filter low quality cells
sc.pp.filter_cells(adata, min_counts=10)
sc.pp.filter_genes(adata, min_cells=5)

### Save raw counts to layers
adata.layers["counts"] = adata.X.copy()

#### Add metadata information for each tissue section

#### save anndata  for each tissue section


# ---- cell 5 ----
import scanpy as sc
import os

# Define base path to your .h5ad files
base_path = "path/anndata"

# Helper to construct full paths
def load_h5ad(filename):
    return sc.read_h5ad(os.path.join(base_path, filename))

# Load all datasets
slide1_BA9_control_304 = load_h5ad("case304_slide1_BA9_control.h5ad")
slide1_BA17_control_304 = load_h5ad("case304_slide1_BA17_control.h5ad")
slide1_BA9_AD_98 = load_h5ad("case98_slide1_BA9_AD.h5ad")
slide1_BA17_AD_98 = load_h5ad("case98_slide1_BA17_AD.h5ad")

slide2_BA9_control_85 = load_h5ad("case85_slide2_BA9_control.h5ad")
slide2_BA17_control_85 = load_h5ad("case85_slide2_BA17_control.h5ad")
slide2_BA9_AD_192 = load_h5ad("case192_slide2_BA9_AD.h5ad")
slide2_BA17_AD_192 = load_h5ad("case192_slide2_BA17_AD.h5ad")

slide3_BA9_control_90 = load_h5ad("case90_slide3_BA9_control.h5ad")
slide3_BA17_control_90 = load_h5ad("case90_slide3_BA17_control.h5ad")
slide3_BA9_AD_194 = load_h5ad("case194_slide3_BA9_AD.h5ad")
slide3_BA17_AD_194 = load_h5ad("case194_slide3_BA17_AD.h5ad")

slide4_BA9_control_302 = load_h5ad("case302_slide4_BA9_control.h5ad")
slide4_BA17_control_302 = load_h5ad("case302_slide4_BA17_control.h5ad")
slide4_BA9_AD_99 = load_h5ad("case99_slide4_BA9_AD.h5ad")
slide4_BA17_AD_99 = load_h5ad("case99_slide4_BA17_AD.h5ad")

# Apply spatial shifts for alignment
slide2_BA17_AD_192.obsm["spatial"][:, 0] += 11479
slide2_BA9_AD_192.obsm["spatial"][:, 0] += 11346
slide2_BA9_control_85.obsm["spatial"][:, 0] += 10946
slide2_BA17_control_85.obsm["spatial"][:, 0] += 11042
slide3_BA9_control_90.obsm["spatial"][:, 0] += 20898
slide3_BA17_control_90.obsm["spatial"][:, 0] += 21293
slide3_BA9_AD_194.obsm["spatial"][:, 0] += 21390
slide3_BA17_AD_194.obsm["spatial"][:, 0] += 20916
slide4_BA9_control_302.obsm["spatial"][:, 0] += 32026
slide4_BA17_control_302.obsm["spatial"][:, 0] += 32781
slide4_BA9_AD_99.obsm["spatial"][:, 0] += 31394

# Concatenate by slide
cat = slide1_BA9_control_304.concatenate(slide1_BA9_AD_98)
cat = cat.concatenate(slide1_BA17_control_304)
cat = cat.concatenate(slide1_BA17_AD_98)

mat = slide2_BA9_control_85.concatenate(slide2_BA9_AD_192)
mat = mat.concatenate(slide2_BA17_control_85)
mat = mat.concatenate(slide2_BA17_AD_192)

sat = slide3_BA9_control_90.concatenate(slide3_BA9_AD_194)
sat = sat.concatenate(slide3_BA17_control_90)
sat = sat.concatenate(slide3_BA17_AD_194)

kat = slide4_BA9_control_302.concatenate(slide4_BA9_AD_99)
kat = kat.concatenate(slide4_BA17_control_302)
kat = kat.concatenate(slide4_BA17_AD_99)

# Combine all slides
data_merged = cat.concatenate(mat)
data_merged = data_merged.concatenate(sat)
data_merged = data_merged.concatenate(kat)

# Save the final merged object
output_path = "merged_spatial_BA9_BA17.h5ad"
data_merged.write(output_path)
print(f"Merged data saved to {output_path}")



### plot the merged data 

sq.pl.spatial_scatter(
   data_merged,
    library_id="spatial",spatial_key='spatial', 
    shape=None,
    color=[
        "Brain.Region",
    ],
    wspace=0.2,figsize=(15,15),label=True
)


# ---- cell 6 ----
"""
This script reads a merged Xenium spatial transcriptomics dataset,
normalizes it, runs dimensionality reduction and clustering, performs
batch correction using Harmony, and assigns cell types manually based
on clustering results.
"""

import os
import scanpy as sc
import scanpy.external as sce
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- Load merged dataset ---
adata = sc.read_h5ad("path/Fulldataset_BA9_BA17.h5ad")

# Set raw counts for processing
adata.X = adata.layers["counts"]

# --- Preprocessing ---
sc.pp.normalize_total(adata, inplace=True)
sc.pp.log1p(adata)
sc.pp.pca(adata)

# --- Batch correction using Harmony ---
sce.pp.harmony_integrate(adata, key='Donor')

# --- Clustering and embedding ---
sc.pp.neighbors(adata, n_pcs=15, n_neighbors=25, use_rep="X_pca_harmony")
sc.tl.leiden(adata, resolution=0.8, key_added="Sub2_0.8")
sc.tl.leiden(adata, resolution=1.0, key_added="Sub2_1.0")
sc.tl.umap(adata, spread=1.2)

# --- Marker gene analysis ---
sc.tl.rank_genes_groups(adata, groupby="Sub2_1.0", method="wilcoxon")
sc.pl.rank_genes_groups(adata, n_genes=25, sharey=False)

# --- Manual annotation of clusters ---
cluster_annotations = {
    "0":  "Oligo_Microglia",
    "1":  "Oligodendrocytes",
    "2":  "Endothelial",
    "3":  "Oligodendrocytes",
    "4":  "Inh_Neurons",
    "5":  "Oligodendrocytes",
    "6":  "Exc_Neurons",
    "7":  "Oligodendrocytes",
    "8":  "Exc_Neurons",
    "9":  "Astrocytes",
    "10": "Microglia",
    "11": "VLMC",
    "12": "Exc_Neurons",
    "13": "Exc_Neurons",
    "14": "Excitatory_mixed",
    "15": "Exc_Neurons",
    "16": "OPC",
    "17": "Oligodendrocytes",
    "18": "Exc_Neurons",
    "19": "Ast_oligo",
    "20": "Inhibitory",
    "21": "Oligo_Endothelial",
    "22": "Oligo_Microglia"
}

adata.obs["major_celltypes_manual"] = (
    adata.obs["Sub2_1.0"].map(cluster_annotations).astype("category")
)

# ---- cell 7 ----
# predict_celltypes_by_top_markers.py

"""
This script assigns predicted cell types to each cell in an AnnData object
based on the top expressed transcripts and predefined marker genes with weights.
"""

import numpy as np
import pandas as pd
import scanpy as sc
from scipy.sparse import issparse

# --- Load AnnData object ---
# NOTE: Replace 'your_data.h5ad' with your actual file path
adata = sc.read_h5ad("your_data.h5ad")

# --- Define marker genes with weights for each cell type ---
cell_type_markers = {
    "Microglia": [("ITGAM", 1), ("LYVE1", 1), ("MRC1", 1), ("ITGAX", 1), 
                  ("PTPRC", 1), ("CX3CR1", 2), ("P2RY12", 2), ("GPNMB", 1), 
                  ("TREM2", 1), ("AIF1", 1), ("CD163", 1)],
    "Astrocytes": [("GFAP", 1), ("AQP4", 2), ("ALDH1L1", 1), ("SLC1A2", 1), 
                   ("FGFR3", 1), ("GJA1", 1), ("FGFR1", 1), ("CHI3L1", 1),
                   ("ID3", 1), ("AQP1", 1)],
    "Oligodendrocytes": [("ERMN", 2), ("MAG", 1), ("MOG", 1), ("MOBP", 1), 
                         ("OPALIN", 1), ("PCSK6", 1), ("ST18", 1), ("NCSTN", 1),
                         ("MAL", 1), ("MYRF", 1)],
    "Exc_Neurons": [("SLC17A7", 2), ("RORB", 1), ("SLC17A6", 1), ("THEMIS", 1),
                    ("CUX2", 1), ("TESPA1", 1), ("NTNG2", 1), ("OTOGL", 1), ("HTR2A", 1)],
    "Inh_Neurons": [("GAD1", 2), ("ADARB2", 1), ("GAD2", 2), ("PVALB", 1),
                    ("VIP", 2), ("SST", 2), ("LAMP5", 1)],
    "Endothelial": [("NOTCH1", 2), ("PECAM1", 2), ("FLT1", 2), ("CEMIP2", 2)],
    "VLMC": [("CEMIP", 2), ("CSPG4", 1), ("DCN", 2)],
    "OPC": [("CSPG4", 2), ("VCAN", 1), ("PDGFRA", 1), ("PTPRZ1", 1), 
            ("BRINP3", 1), ("ITGA8", 1)]
}

# --- Prepare expression matrix ---
if issparse(adata.X):
    adata.X = adata.X.toarray()

# Parameters
top_n = 20  # Top N genes per cell

# Initialize outputs
adata.obs["predicted_cell_type"] = "Unknown"
adata.obs["prediction_confidence"] = 0.0
adata.obs["top_transcripts"] = ""
adata.obs["matched_transcripts"] = ""
cell_type_match_counts = pd.DataFrame(index=adata.obs.index, columns=cell_type_markers.keys(), dtype=int).fillna(0)

# --- Process each cell ---
for cell in adata.obs.index:
    cell_expr = adata[cell, :].X.flatten()
    sorted_indices = np.argsort(cell_expr)[::-1][:top_n]
    
    top_genes = adata.var_names[sorted_indices]
    top_expr = cell_expr[sorted_indices]
    top_transcripts_str = ','.join([f"{gene}({expr:.2f})" for gene, expr in zip(top_genes, top_expr)])
    adata.obs.at[cell, "top_transcripts"] = top_transcripts_str

    matched_transcripts = []
    cell_scores = {ctype: 0.0 for ctype in cell_type_markers}

    for ctype, markers in cell_type_markers.items():
        match_count = 0
        for gene, weight in markers:
            if gene in top_genes:
                gene_idx = np.where(adata.var_names == gene)[0][0]
                expr_val = cell_expr[gene_idx]
                if expr_val > 0:
                    cell_scores[ctype] += expr_val * weight
                    matched_transcripts.append(f"{gene}({expr_val:.2f})")
                    match_count += 1
        cell_type_match_counts.at[cell, ctype] = match_count

    adata.obs.at[cell, "matched_transcripts"] = ','.join(matched_transcripts)
    best_ctype = max(cell_scores, key=cell_scores.get)
    max_score = cell_scores[best_ctype]
    total_score = sum(cell_scores.values())
    confidence = max_score / total_score if total_score > 0 else 0.0

    adata.obs.at[cell, "predicted_cell_type"] = best_ctype
    adata.obs.at[cell, "prediction_confidence"] = confidence

# --- Merge match counts into obs ---
adata.obs = pd.concat([adata.obs, cell_type_match_counts], axis=1)
adata.obs=adata.obs.astype("str")
# Optional: Save annotated data
adata.write("adata_with_predicted_celltypes.h5ad")



# ---- cell 8 ----
# celltype_transfer_allen_to_spatial.py

"""
This script transfers cell type annotations from a reference Allen single-nucleus RNA-seq dataset
to a merged Xenium spatial transcriptomics dataset using a deep learning model.

The script `celltype_transfer_allen_to_spatial.py` performs the following:
- Loads and processes Allen DLPFC scRNA-seq reference data
- Aligns genes with spatial Xenium data
- Transfers annotations using `spatialid.Transfer`
- Predicts major cell types in spatial data
- Visualizes the predicted types using Squidpy

"""

# --- Imports ---
import os
import scanpy as sc
import scanpy.external as sce
import anndata
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from spatialid import Transfer
import torch
import torch_cluster
import squidpy as sq

# --- Load Reference Data (Allen DLPFC) ---
allen_path = "/oak/stanford/groups/icobos/Akila/Akila_Download_AWS/SEAAD_A9_RNAseq_final-nuclei.2024-02-13.h5ad"
allen_DLPFC = sc.read_h5ad(allen_path)
ref = allen_DLPFC

# --- Map fine-grained subclasses to broader cell types ---
new_clust = {
    "L2/3 IT": "Exc_Neurons", "L5 IT": "Exc_Neurons", "L4 IT": "Exc_Neurons",
    "L6 IT": "Exc_Neurons", "L6 CT": "Exc_Neurons", "L5/6 NP": "Exc_Neurons",
    "L6b": "Exc_Neurons", "L6 IT Car3": "Exc_Neurons", "L5 ET": "Exc_Neurons",
    "Pvalb": "Inh_Neurons", "Vip": "Inh_Neurons", "Sst": "Inh_Neurons",
    "Lamp5": "Inh_Neurons", "Sncg": "Inh_Neurons", "Lamp5 Lhx6": "Inh_Neurons",
    "Chandelier": "Inh_Neurons", "Pax6": "Inh_Neurons", "Sst Chodl": "Inh_Neurons",
    "Astrocyte": "Astrocyte", "Microglia-PVM": "Microglia", "Oligodendrocyte": "Oligodendrocytes",
    "OPC": "OPC", "VLMC": "VLMC", "Endothelial": "Endothelial"
}

ref.obs['major_celltypes_allen'] = ref.obs['Subclass'].map(new_clust).astype('category')
sc_data = ref  # Single-cell reference data

# --- Load Spatial Data (merged Xenium dataset) ---
# Make sure `st_data` is loaded before this script is run
# Example: st_data = sc.read_h5ad("path/to/merged_xenium_data.h5ad")

# --- Harmony integration of scRNA-seq reference ---
sce.pp.harmony_integrate(sc_data, ['Donor ID'])

# --- Filter low-quality genes and cells ---
sc.pp.filter_cells(sc_data, min_genes=2)
sc.pp.filter_genes(sc_data, min_cells=2)
sc.pp.filter_cells(st_data, min_genes=25)

# --- Match common genes between scRNA-seq and spatial data ---
common_genes = sc_data.var_names.intersection(st_data.var_names)
sc_data = sc_data[:, common_genes]
st_data = st_data[:, common_genes]

print(f"Aligned genes: {len(common_genes)}")
print(f"scRNA-seq shape: {sc_data.shape}")
print(f"Spatial data shape: {st_data.shape}")

# --- Set output directory ---
output_dir = "/scratch/groups/icobos/Akila/transfer_learning/output_major/"
os.makedirs(output_dir, exist_ok=True)

# --- Transfer Learning with SpatialID ---
transfer = Transfer(
    spatial_data=st_data,
    single_data=sc_data,
    output_path=output_dir,
    device=0  # GPU index; set to -1 for CPU
)

transfer.learn_sc(
    sc_data=sc_data,
    filter_mt=False,
    min_cell=2,
    min_gene=2,
    max_cell=100,
    ann_key="major_celltypes_allen",
    batch_size=512,
    epoch=400,
    lr=1e-4
)

transfer.sc2st()
print(st_data.obs["pseudo_class"].value_counts())

# --- Graph-based Annotation ---
transfer.annotation(
    pca_dim=100,
    n_neigh=30,
    edge_weight=True,
    epochs=200,
    lr=0.01,
    weight_decay=1e-4,
    w_cls=20.0,
    w_dae=1.0,
    w_gae=1.0,
    show_results=True
)

print(st_data.obs["celltype_pred"].value_counts())

# --- Transfer cell types back to original merged anndata ---
# 'bdata' is the unfiltered spatial dataset 
# Example: bdata = sc.read_h5ad("path/to/full_merged_spatial_data.h5ad")

adata = st_data
cell_types = pd.Series('unknown', index=bdata.obs.index)

# Fill known predictions
common_index = adata.obs.index.intersection(bdata.obs.index)
cell_types.loc[common_index] = adata.obs.loc[common_index, 'celltype_pred']
bdata.obs['DNN_cell_type'] = cell_types

# --- Visualize with Squidpy ---
sq.pl.spatial_scatter(
    bdata,
    library_id="spatial",
    spatial_key="spatial",
    color=["DNN_cell_type"],
    shape=None,
    wspace=0.2,
    figsize=(15, 15),
    cmap="tab20"
)


# ---- cell 9 ----
# label_transfer_allen_ingest.py

"""
This script transfers major cell type labels from the Allen DLPFC single-nucleus RNA-seq reference dataset
to Xenium spatial transcriptomics data using Scanpy's `ingest` function.
"""

# --- Imports ---
import scanpy as sc
import scanpy.external as sce
import squidpy as sq
import anndata as ad

# --- Load data ---
# Replace these lines with your actual data loading steps
# Example:
# adata_nucleus = sc.read_h5ad("path/to/allen_reference.h5ad")
# adata_xenium = sc.read_h5ad("path/to/xenium_data.h5ad")

# These should be pre-loaded before running the script
# adata_nucleus: AnnData object with Allen reference data
# adata_xenium: Merged Xenium spatial dataset

# --- Match genes between reference and spatial data ---
common_genes = adata_nucleus.var_names.intersection(adata_xenium.var_names)
adata_nucleus = adata_nucleus[:, common_genes].copy()
adata_xenium = adata_xenium[:, common_genes].copy()

# --- PCA and Harmony integration on Allen reference ---
sc.tl.pca(adata_nucleus)
sce.pp.harmony_integrate(adata_nucleus, key='Donor ID')
adata_nucleus.obsm['X_pca'] = adata_nucleus.obsm['X_pca_harmony']

# --- Build neighbor graph for ingest to use ---
sc.pp.neighbors(adata_nucleus, n_neighbors=20, n_pcs=18)

# Ensure the target annotation column exists
adata_nucleus.obs['ingest_transfer_allen_major_celltypes'] = adata_nucleus.obs['major_celltypes_allen']

# --- Transfer labels donor-by-donor from reference to Xenium ---
xenium_donors = adata_xenium.obs['metadata'].unique()
xenium_results = []

for donor in xenium_donors:
    print(f"Transferring labels for Xenium donor: {donor}")
    
    xenium_donor = adata_xenium[adata_xenium.obs['metadata'] == donor].copy()
    sc.tl.ingest(
        xenium_donor,
        adata_nucleus,
        obs='ingest_transfer_allen_major_celltypes',
        embedding_method='pca'
    )
    
    xenium_donor.obs["metadata"] = donor
    xenium_results.append(xenium_donor)

# --- Combine all donors ---
adata_xenium_transferred = ad.concat(xenium_results)

# --- Visualize spatial cell type predictions ---
sq.pl.spatial_scatter(
    adata_xenium_transferred,
    library_id="spatial",
    spatial_key='spatial',
    shape=None,
    color=["ingest_transfer_allen_major_celltypes"],
    wspace=0.2,
    figsize=(15, 15),
    cmap="tab10"
)


# ---- cell 10 ----
import pandas as pd

# --- Define annotation methods used for consensus ---
methods = ['major_celltypes_manual', 'predicted_cell_type', 'DNN_cell_type', 'ingest_transfer_allen_major_celltypes']

# --- Subset the relevant annotation columns ---
label_df = adata.obs[methods]

# --- Compute consensus confidence per cell ---
def get_consensus_confidence(row):
    counts = row.value_counts(dropna=True)
    if counts.empty:
        return 0.0
    top_count = counts.iloc[0]
    return top_count / len(row)

# --- Apply to each row to calculate consensus confidence ---
adata.obs['consensus_confidence'] = label_df.apply(get_consensus_confidence, axis=1)

# --- Compute the ensemble (majority-vote) label ---
# In case of a tie, mode() returns multiple values; take the first one
adata.obs['ensemble_label'] = label_df.mode(axis=1)[0]



# ---- cell 11 ----
import scanpy as sc
import scanpy.external as sce
import squidpy as sq
import anndata as ad

def preprocess_xenium_excitatory(adata_xenium, region, adata_nucleus):
    """
    Preprocess Xenium data for a specific brain region and perform label transfer
    using reference single-nucleus data.
    """
    print(f"\n### Processing region: {region} ###")

    # Subset to excitatory neurons in the specified region
    adata_exc = adata_xenium[adata_xenium.obs["ensemble_label"] == "Exc_Neurons"]
    adata_region = adata_exc[adata_exc.obs["Brain.Region"] == region]

    # Filter low-quality cells
    adata_region = adata_region[
        (adata_region.obs["consensus_confidence"] > 0.5) &
        (adata_region.obs["transcript_counts"] > 50)
    ]

    # Harmony batch correction on reference nucleus data
    sc.tl.pca(adata_nucleus)
    sce.pp.harmony_integrate(adata_nucleus, key='Donor')
    adata_nucleus.obsm['X_pca'] = adata_nucleus.obsm['X_pca_harmony']
    adata_nucleus.obs['ingest_transfer_sample'] = adata_nucleus.obs['Author_Annotation']

    # Ingest label transfer for each Xenium donor
    xenium_donors = adata_region.obs['metadata'].unique()
    xenium_results = []

    for donor in xenium_donors:
        print(f"Transferring labels for Xenium donor: {donor}")
        xenium_donor = adata_region[adata_region.obs['metadata'] == donor].copy()

        sc.tl.ingest(
            xenium_donor,
            adata_nucleus,
            obs='ingest_transfer_sample',
            embedding_method='pca'
        )

        xenium_donor.obs["metadata"] = donor
        xenium_results.append(xenium_donor)

    # Combine results from all donors
    adata_combined = ad.concat(xenium_results)

    # Plot spatial results
    sq.pl.spatial_scatter(
        adata_combined,
        library_id="spatial",
        spatial_key='spatial',
        shape=None,
        color=["ingest_transfer_sample"],
        wspace=0.2,
        figsize=(15, 15),
        cmap="tab20"
    )

    return adata_combined


# Reference nucleus data
adata_nucleus_BA9 = BA9_exc
adata_nucleus_BA17 = BA17_exc

# Run for BA9 region
adata_xenium_BA9 = preprocess_xenium_excitatory(adata_xenium, "BA9", adata_nucleus_BA9)

# Run for BA17 region
adata_xenium_BA17 =preprocess_xenium_excitatory(adata_xenium, "BA17", adata_nucleus_BA17)


# ---- cell 12 ----
import scanpy as sc
import scanpy.external as sce
import squidpy as sq
import anndata as ad

def preprocess_xenium_inhibitory(adata_xenium, region, adata_nucleus):
    """
    Preprocess Xenium inhibitory neuron data for a specific brain region and perform label transfer
    using reference single-nucleus inhibitory data.
    """
    print(f"\n### Processing Inhibitory Neurons for region: {region} ###")

    # Subset to inhibitory neurons in the specified region
    adata_inh = adata_xenium[adata_xenium.obs["ensemble_label"] == "Inh_Neurons"]
    adata_region = adata_inh[adata_inh.obs["Brain.Region"] == region]

    # Filter low-quality cells
    adata_region = adata_region[
        (adata_region.obs["consensus_confidence"] > 0.5) &
        (adata_region.obs["transcript_counts"] > 50)
    ]

    # Harmony batch correction on reference nucleus data
    sc.tl.pca(adata_nucleus)
    sce.pp.harmony_integrate(adata_nucleus, key='Donor')
    adata_nucleus.obsm['X_pca'] = adata_nucleus.obsm['X_pca_harmony']
    adata_nucleus.obs['ingest_transfer_sample'] = adata_nucleus.obs['Author_Annotation']

    # Ingest label transfer for each Xenium donor
    xenium_donors = adata_region.obs['metadata'].unique()
    xenium_results = []

    for donor in xenium_donors:
        print(f"Transferring labels for Xenium donor: {donor}")
        xenium_donor = adata_region[adata_region.obs['metadata'] == donor].copy()

        sc.tl.ingest(
            xenium_donor,
            adata_nucleus,
            obs='ingest_transfer_sample',
            embedding_method='pca'
        )

        xenium_donor.obs["metadata"] = donor
        xenium_results.append(xenium_donor)

    # Combine results from all donors
    adata_combined = ad.concat(xenium_results)

    # Plot spatial results
    sq.pl.spatial_scatter(
        adata_combined,
        library_id="spatial",
        spatial_key='spatial',
        shape=None,
        color=["ingest_transfer_sample"],
        wspace=0.2,
        figsize=(15, 15),
        cmap="tab20"
    )

    return adata_combined


# Reference inhibitory single-nucleus data
adata_nucleus_BA9_inh = BA9_inh
adata_nucleus_BA17_inh = BA17_inh

# Run for BA9 inhibitory population
adata_xenium_BA9_inh = preprocess_xenium_inhibitory(adata_xenium, "BA9", adata_nucleus_BA9_inh)

# Run for BA17 inhibitory population
adata_xenium_BA17_inh = preprocess_xenium_inhibitory(adata_xenium, "BA17", adata_nucleus_BA17_inh)


