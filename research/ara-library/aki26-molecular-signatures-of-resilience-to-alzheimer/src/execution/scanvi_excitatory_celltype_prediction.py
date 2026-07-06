# Grounding: transcribed
# Source: scANVI_excitatory_celltype_prediction.ipynb (author repo AkilaRanjith/Molecular-Signatures-of-Resilience...); code cells only (outputs stripped).

# ---- cell 1 ----
import scanpy as sc


### read the excitatory neuronal population
bdata=sc.read_h5ad("path/dataset.h5ad")
exc=bdata[bdata.obs['major_celltypes'].isin(["Excitatory"])]

#### preprocess
sc.pp.normalize_total(exc, target_sum=1e4)
sc.pp.log1p(exc)
exc.uns['log1p']["base"] = None


# Perform differential expression analysis using Wilcoxon rank-sum test for excitatory clusters
sc.tl.rank_genes_groups(exc, groupby='Author_Annotation',method='wilcoxon',pts=True,corr_method='benjamini-hochberg')
sc.tl.filter_rank_genes_groups(exc,min_in_group_fraction=0.1,min_fold_change=0.6)

# Get the top differentially expressed genes for each class
top_genes_per_class = []
for label in exc.obs['Author_Annotation'].unique():
    top_genes = exc.uns['rank_genes_groups_filtered']['names'][label][:200]
    top_genes_per_class.extend(top_genes)

# Get unique top genes across all classes
top_genes_unique = list(set(top_genes_per_class))
df = pd.DataFrame(top_genes_unique)
celltype_pattern=df
df.to_csv("excitatory_genes.csv")

# ---- cell 2 ----
#### calculate the highly variable genes

sc.pp.highly_variable_genes(exc,flavor="seurat_v3",n_top_genes=2000)

highly_variable_genes = exc.var_names[exc.var['highly_variable']]

# Create the combined gene list HVG and celltype marker genes 
genes_subset = np.concatenate([highly_variable_genes, celltype_pattern])

# Get the intersection of the gene list 
genes_present = np.intersect1d(genes_subset, exc.var_names)

# Subset the AnnData object only for the present genes
subset_adata = exc[:, genes_present]



# ---- cell 3 ----
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scanpy as sc
import scvi
from scvi.model.utils import mde
import scanpy.external as sce
import anndata
from scipy.io import mmread
from sklearn.decomposition import TruncatedSVD
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import torch


scvi.settings.seed = 0


##### load the subset excitatory anndata (var names include only HVG and cell type_pattern)

ref_adata= subset_adata
adata=ref_adata
adata.X=adata.layers["counts"]
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)


#### specify the reference data

adata.obs["ds_ID"]="ref"

# Specifying the model for batch effect.
batch_keys = ['ds_ID', 'Assay', 'subject','Brain.Region']

combined_batch_key = '-'.join(batch_keys)

adata.obs[combined_batch_key] = adata.obs[batch_keys].astype(str).agg('-'.join, axis=1)

# Setup the AnnData object for scvi-tools use raw counts
scvi.model.SCVI.setup_anndata(adata, layer="counts", batch_key=combined_batch_key)
vae = scvi.model.SCVI(adata, n_layers=2, n_latent=30)
vae.train(max_epochs=200,check_val_every_n_epoch=50)


#### plot the reconstruction loss
fig = plt.gcf()
fig.set_size_inches(8, 8)
fig.set_dpi(500)
history_df = (
  vae.history['reconstruction_loss_train'].astype(float)
   
    .reset_index()
    .melt(id_vars = ['epoch'])
)

ax=history_df.plot(x='epoch', y='value', color='black', marker='o', linestyle='-', linewidth=2)
ax.set_xlabel("Epoch")
ax.set_ylabel("Reconstruction Loss (Test)")


#### save the training model

vae.save("/celltypesignature/train/")


######scANVI prediction#######

ref_data=sc.read_h5ad("path/data.h5ad")

ref_data.obs["ds_ID"]="ref"

# Specifying the model.
batch_keys = ['ds_ID', 'Assay', 'subject','Brain.Region']

combined_batch_key = '-'.join(batch_keys)

ref_data.obs[combined_batch_key] = ref_data.obs[batch_keys].astype(str).agg('-'.join, axis=1)

####  load training model
vae= scvi.model.SCVI.load("path/train/",ref_data)



ref_data.obs["celltype_scanvi"] = ref_data.obs["Author_Annotation"].values

#### scANVI prediction linear perceptron

vae_ref_scan = scvi.model.SCANVI.from_scvi_model(
    vae,
    unlabeled_category="Unknown",
    labels_key="celltype_scanvi",linear_classifier=True, 
    var_activation=torch.nn.functional.softplus,n_latent=30,n_layers=2
)

#### SCANVI model train
vae_ref_scan.train(max_epochs=400, n_samples_per_label=1000,
          early_stopping_monitor='elbo_validation',
          early_stopping_patience=50)


#### plot the reconstruction loss

fig = plt.gcf()
fig.set_size_inches(8, 8)
fig.set_dpi(500)
history_df = (
  vae_ref_scan.history['reconstruction_loss_train'].astype(float)
   
    .reset_index()
    .melt(id_vars = ['epoch'])
)

ax=history_df.plot(x='epoch', y='value', color='black', marker='o', linestyle='-', linewidth=2)
ax.set_xlabel("Epoch")
ax.set_ylabel("Reconstruction Loss")

#### save the pre trained model for prediction

vae_ref_scan.save("path/pretrain/")


#### save the prediction probability from classifier to dataframe 

softprediction = vae_ref_scan.predict(ref_data,soft=True)
df=softprediction
softprediction.to_csv("path/softprediction.csv")

# ---- cell 4 ----
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



#### read the softprediction values from dataframe
df=pd.read_csv("/celltypesignature/softprediction.csv")

#### Assign for each cell maxium prediction probability score from dataframe 
# Find maximum values for numeric columns
numeric_cols = df.select_dtypes(include='number').columns
max_values = df[numeric_cols].max(axis=1)

# Find column name for maximum values
max_columns = df[numeric_cols].idxmax(axis=1)

# Add information to the dataframe

### max_value denotes the prediction probability and max_colum denotes the predicted celltype
df['max_value'] = max_values
df['max_column'] = max_columns


#### Add this prediction probability information and the celltype prediction to anndata 

#### read the excitatory anndata including all the gene names

df = df.set_index(exc.obs_names)

# Check if the length of the values matches the number of cells in the AnnData object
if len(df) != exc.n_obs:
    raise ValueError("Length of passed value for obs_names does not match the number of cells in AnnData object.")

# Add the columns from the dataframe to the 'obs' attribute of the AnnData object
exc.obs[df.columns] = df

#### reference_label denotes the celltype from scanpy clustering
exc.obs['reference_label']=exc.obs['Author_Annotation']

df = exc.obs
confusion_matrix = pd.crosstab(
    df["max_column"],
    df["Author_Annotation"],
    rownames=["max_column"],
    colnames=["Author_Annotation"],
)

### confusion matrix
confusion_matrix /= confusion_matrix.sum(1).ravel().reshape(-1, 1)

# Reorder the confusion matrix based on the row labels

order=['Ex1:[CUX2-SERPINE2-LAMP5]', 'Ex2:[CUX2-RORB-GLIS3-LRRC2]',
    'Ex3:[CUX2-RORB-GLIS3-SV2C]', 'Ex4:[CUX2-RORB-COL5A2-CLMN]',
    'Ex5:[RORB-CUX2-EYA4]', 'Ex6:[RORB-MME]', 'Ex7:[RORB-GABRG1]',
    'Ex8:[RORB-TLL1-TMTC4]', 'Ex9:[RORB-TLL1-PCP4-MID1]','Ex10:[RORB-TLL1-PCP4-TYR]', 'Ex11:[RORB-ADGRL4]', 'Ex12:[THEMIS-PRRX1]',
    'Ex13:[THEMIS-POSTN]', 'Ex14:|FEZF2-HTR2C]', 'Ex15:[FEZF2-ADRA1A]',
    'Ex16:[FEZF2-SYT6]', 'Ex17:[FEZF2-ZFHX3-SEMA3D]', 'Ex18:[FEZF2-ZFHX3-SCUBE1]']

confusion_matrix = confusion_matrix.reindex(index=order, columns=order)

####  plot the confidence score for each excitatory celltype
fig, ax = plt.subplots(figsize=(15, 15))
sns.heatmap(
    confusion_matrix,
    cmap="viridis",
    ax=ax,
    square=True,
    cbar_kws=dict(shrink=0.3, aspect=12),
)
ax.set_aspect('equal', adjustable='box')
plt.yticks(rotation=0)  # Rotate y-labels to prevent cutoff

# Label confidence scores above 0.5
for i in range(confusion_matrix.shape[0]):
    for j in range(confusion_matrix.shape[1]):
        if confusion_matrix.iloc[i, j] > 0.5:
            ax.text(j + 0.5, i + 0.5, f"{confusion_matrix.iloc[i, j]:.2f}",
                    ha='center', va='center', color='white', fontsize=14)
plt.savefig("/confidence_plot.pdf",dpi=500)     

# ---- cell 5 ----
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scanpy as sc
import scvi
from scvi.model.utils import mde
import scanpy.external as sce
import anndata
from scipy.io import mmread
from sklearn.decomposition import TruncatedSVD
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import torch

scvi.settings.seed = 0

### read the query data for prdiction query=DLPFC
DLPFC=sc.read_h5ad("path/dlpfc.h5ad")
adata_query=DLPFC

# Specifying the model.
batch_keys = ['ds_ID', 'Assay', 'subject','Brain.Region']

combined_batch_key = '-'.join(batch_keys)

adata_query.obs[combined_batch_key] = adata_query.obs[batch_keys].astype(str).agg('-'.join, axis=1)

#### prepare query data
scvi.model.SCANVI.prepare_query_anndata(adata_query, "path/pretrain")


#### load the pretrained model and predict the query data
vae_q = scvi.model.SCANVI.load_query_data(
    adata_query,
    "path/pretrain",
)
vae_q.train(
    max_epochs=200,
    plan_kwargs=dict(weight_decay=0.0),
    check_val_every_n_epoch=10
)

#### plot the elbow plot for validation 
fig = plt.gcf()
fig.set_size_inches(8, 8)
fig.set_dpi(500)
history_df = (
  vae_q.history['reconstruction_loss_train'].astype(float)
   
    .reset_index()
    .melt(id_vars = ['epoch'])
)

ax=history_df.plot(x='epoch', y='value', color='black', marker='o', linestyle='-', linewidth=2)
ax.set_xlabel("Epoch")
ax.set_ylabel("Reconstruction Loss")

#### save the query prediction probability from linear classifier
softprediction = vae_q.predict(adata_query,soft=True)
softprediction.to_csv("/DLPFC/softprediction.csv")

# ---- cell 6 ----

#### load the excitatory data after adding the pre trained model prediction information

exc.uns['log1p']["base"] = None

#### mention the max_column slot which denotes the cell type prediction from the pre trained model.

sc.tl.rank_genes_groups(exc,"max_column",method='wilcoxon',pts=True,corr_method='benjamini-hochberg')
sc.tl.filter_rank_genes_groups(exc,min_in_group_fraction=0.2,min_fold_change=0.6)
sc.pl.rank_genes_groups_dotplot(exc,n_genes=5,key='rank_genes_groups_filtered')

# ---- cell 7 ----
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_distances

##### subset the EX5 cell type from reference data and DLPFC data

### refdata
adata1=exc[exc.obs["Author_Annotation"].isin(["Ex5:[RORB-CUX2-EYA4]"])]
#### DLPFC data after adding pretrained model prediction information
adata2=DLPFC[DLPFC.obs["max_column"].isin(["Ex5:[RORB-CUX2-EYA4]"])]

# Convert sparse matrices to CSR format 
expr_matrix1 = csr_matrix(adata1[:, common_genes].X)
expr_matrix2 = csr_matrix(adata2[:, common_genes].X)

# Compute cosine similarity between cells in the two datasets
cosine_dist_matrix = cosine_distances(expr_matrix2, expr_matrix1)

# Calculate cell-wise similarity scores

average_similarity_scores = 1 - np.mean(cosine_dist_matrix, axis=1)

threshold = 0.3  # Adjust the threshold 
similar_pairs = np.argwhere(cosine_dist_matrix < threshold)

# Print  results
print("Average similarity scores:", average_similarity_scores)
print("Pairs of similar cells:", similar_pairs)


#### plot the average distance similarity scores between two datsete
plt.figure(figsize=(8, 6))
sns.histplot(average_similarity_scores, kde=True, color='green')
plt.title('Distribution of cosine Average distance Scores')
plt.xlabel('Average cosine distance Score')
plt.ylabel('Frequency')

plt.savefig("/cosine_distance.pdf")
plt.show()

