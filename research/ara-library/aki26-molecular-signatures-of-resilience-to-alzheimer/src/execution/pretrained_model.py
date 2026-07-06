# Grounding: transcribed
# Source: pretrained_model.ipynb (author repo AkilaRanjith/Molecular-Signatures-of-Resilience...); code cells only (outputs stripped).

# ---- cell 1 ----
#### Excitatory neuronal subset prediction ######

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


#### Load excitatory  subset data in h5ad format based (Run QC, major celltype annotation and mark potential doublets remove them)
Exc=sc.read_h5ad("filepath"/ exc.h5ad)

                 
####prerequist columns in observation slot (subject,ds_ID,Brain.Region,Assay) 
#### ds_ID in observation slot 
                 
exc.obs["ds_ID"]="query"

###store raw counts in counts layers                  
exc.layers["counts"]=exc.raw.X                
                                  
adata_query=exc


# Specifying the model .
batch_keys = ['ds_ID', 'Assay', 'subject','Brain.Region']

combined_batch_key = '-'.join(batch_keys)

adata_query.obs[combined_batch_key] = adata_query.obs[batch_keys].astype(str).agg('-'.join, axis=1)
scvi.model.SCANVI.prepare_query_anndata(adata_query, "path to downloaded pretrained exc model")
vae_q = scvi.model.SCANVI.load_query_data(
    adata_query,
    "path to downloaded pretrained exc model"",
)
vae_q.train(
    max_epochs=200,n_samples_per_label=2000,
    plan_kwargs=dict(weight_decay=0.0),
    check_val_every_n_epoch=10
)
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
ax.set_ylabel("Reconstruction Loss (Test)")

# Save the plot with adjusted size and DPI
plt.savefig("reconstruction_train.pdf", bbox_inches='tight')

softprediction = vae_q.predict(adata_query,soft=True)
softprediction.to_csv("exc_softprediction.csv")



# Inhibitory neuronal subset prediction
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


#### Load Inhibitory subset data in h5ad format based (Run QC, major celltype annotation and mark potential doublets remove them)
inh=sc.read_h5ad("filepath"/ inh.h5ad)

                 
####prerequist columns in observation slot (subject,ds_ID,Brain.Region,Assay) 
#### ds_ID in observation slot 
                 

inh.obs["ds_ID"]="query"
                 
###store raw counts in counts layers                  
inh.layers["counts"]=inh.raw.X                   
                 
                 
adata_query=inh


# Specifying the model.
batch_keys = ['ds_ID', 'Assay', 'subject','Brain.Region']

combined_batch_key = '-'.join(batch_keys)

adata_query.obs[combined_batch_key] = adata_query.obs[batch_keys].astype(str).agg('-'.join, axis=1)
scvi.model.SCANVI.prepare_query_anndata(adata_query, "path to downloaded pretrained inh model")
vae_q = scvi.model.SCANVI.load_query_data(
    adata_query,
    "path to downloaded pretrained inh model"",
)
vae_q.train(
    max_epochs=200,n_samples_per_label=2000,
    plan_kwargs=dict(weight_decay=0.0),
    check_val_every_n_epoch=10
)
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
ax.set_ylabel("Reconstruction Loss (Test)")

# Save the plot with adjusted size and DPI
plt.savefig("inh_reconstruction_train.pdf", bbox_inches='tight')

softprediction = vae_q.predict(adata_query,soft=True)
softprediction.to_csv("inh_softprediction.csv")

