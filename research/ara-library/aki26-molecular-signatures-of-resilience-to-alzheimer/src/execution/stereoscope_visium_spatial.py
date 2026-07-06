# Grounding: transcribed
# Source: stereoscope_visium_spatial.ipynb (author repo AkilaRanjith/Molecular-Signatures-of-Resilience...); code cells only (outputs stripped).

# ---- cell 1 ----
####read single nuclei data and do preprocess

sc_adata = sc.read_h5ad("path/dataset.h5ad")
sc.pp.filter_genes(sc_adata, min_counts = 10)
sc.pp.normalize_total(sc_adata, target_sum = 1e5)
sc.pp.log1p(sc_adata)


### read visium data and preprocess
st_adata=sc.read_h5ad("path/Visium_harmony.h5ad")
st_adata.X=st_adata.layers['counts']
st_adata.var_names_make_unique()

##Filter the gene names (spatial/singe cell)
intersect = np.intersect1d(sc_adata.var_names, st_adata.var_names)
st_adata = st_adata[:, intersect].copy()
sc_adata = sc_adata[:, intersect].copy()


### setup anndata and train the latent variable-negative binoial model/deconvlution specify the raw counts in layer slot
#### specify labels_key -"Author_Annotation"

RNAStereoscope.setup_anndata(sc_adata, layer = "unspliced", labels_key = "Author_Annotation")
train = True
if train:
    sc_model = RNAStereoscope(sc_adata)
    sc_model.train(max_epochs = 200)
    sc_model.history["elbo_train"][10:].plot()
    sc_model.save("scmodel", overwrite=True)
else:
    sc_model = RNAStereoscope.load("scmodel", adata=sc_adata)
    print("Loaded RNA model from file!")
    
    
### setup anndata and train visium data 
SpatialStereoscope.setup_anndata(st_adata, layer="counts")
train=True
if train:
    spatial_model = SpatialStereoscope.from_rna_model(st_adata, sc_model)
    spatial_model.train()
    spatial_model.save("stmodel", overwrite = True)
else:
    spatial_model = SpatialStereoscope.load("stmodel", adata=st_adata)
    print("Loaded Spatial model from file!")
    
st_adata.write("path/st_adata.h5ad")
sc_adata.write("path/sc_adata.h5ad")

st_adata.obsm["deconvolution"] = spatial_model.get_proportions()

# Deconvolution
for ct in st_adata.obsm["deconvolution"].columns:
    st_adata.obs[ct] = st_adata.obsm["deconvolution"][ct]
    
#### load the spatial model    
st_adata=sc.read_h5ad("path/st_adata.h5ad")
spatial_model = SpatialStereoscope.load("stereoscope/stmodel", adata=st_adata)





# ---- cell 2 ----
celltypes=["Ex1:[CUX2-SERPINE2-LAMP5]",	"Ex2:[CUX2-RORB-GLIS3-LRRC2]",	"Ex3:[CUX2-RORB-GLIS3-SV2C]",	"Ex4:[CUX2-RORB-COL5A2-CLMN]",	"Ex5:[RORB-CUX2-EYA4]",	"Ex6:[RORB-MME]",	"Ex7:[RORB-GABRG1]",	"Ex8:[RORB-TLL1-TMTC4]",	"Ex9:[RORB-TLL1-PCP4-MID1]",	"Ex10:[RORB-TLL1-PCP4-TYR]",	"Ex11:[RORB-ADGRL4]",	"Ex12:[THEMIS-PRRX1]",	"Ex13:[THEMIS-POSTN]",	"Ex14:|FEZF2-HTR2C]",	"Ex15:[FEZF2-ADRA1A]",	"Ex16:[FEZF2-SYT6]",	"Ex17:[FEZF2-ZFHX3-SEMA3D]",	"Ex18:[FEZF2-ZFHX3-SCUBE1]",	"In1:[LHX6-PVALB-CLMN]",	"In2:[LHX6-PVALB-MEPE]",	"In3:[LHX6-PVALB-COL15A1]",	"In4:[LHX6-SST-MSR1]",	"In5:[LHX6-SST-SPON1]",	"In6:[LHX6-SST-SLC9A2]",	"In7:[LHX6-SST-B3GAT2]",	"In8:[LHX6-SST-SEL1L3]",	"In9:[LHX6-SST-NPY]",	"In10:[LHX6-ADARB2-LAMP5-HCRTR2]",	"In11:[ADARB2-LAMP5-KIT]",	"In12:[ADARB2-LAMP5-NDNF]",	"In13:[ADARB2-SYT6]",	"In14:[ADARB2-SEMA3C]",	"In15:[ADARB2-VIP-DACH2]",	"In16:[ADARB2-VIP-TAC3-NRP1]",	"In17:[ADARB2-VIP-ABI3BP]",	"In18:[ADARB2-VIP-EXPH5]",	"In19:[ADARB2-CALB2-SCML4]",	"Astrocyte-GFAP-OSMR",	"Astrocyte-GFAP-VCAN",	"Astrocyte-SLC1A2-SMTN",	"Astrocyte-SLC1A2-WIF1",	"endothelial",	"Microglia-Homeostatic-CX3CR1",	"Microglia-Reactive-AIF1",	"Microglia-Reactive-CACNA1B",	"Microglia-Reactive-CD163",	"Oligodendrocyte-COL18A1",	"Oligodendrocyte-OPALIN",	"OPC",	"Pericytes",	"VLMC"]

### specify the samples
samples=["Pool_1_100F","Pool_2_100V","Pool_1_35F",	"Pool_1_73F",	"Pool_2_103P",	"Pool_1_35P",	"Pool_1_114F",	"Pool_1_73P",	"Pool_1_124F",	"Pool_2_74P",	"Pool_2_100P",	"Pool_2_74F",	"Pool_2_100M",	"Pool_1_103F"]

import warnings
import scanpy as sc
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")
figsize = (6, 6)  # Adjust the size as per your preference
plt.rcParams.update({'font.size': 15})
sc.settings.figdir = "path/Figures/stereoscope/"

for i in range(len(samples)):
    sp_adata = st_adata[st_adata.obs["sample"].isin([samples[i]])]
    print(samples[i])

    # Get the unique celltypes
    unique_celltypes = celltypes

    # Iterate over celltypes and create a separate figure for each
    for j, celltype in enumerate(unique_celltypes):
        # Create a new figure and axes with equal aspect ratio
        fig, ax = plt.subplots(figsize=figsize)
        ax.set_aspect('equal')
        
        # Plot the embedding for the current celltype on the axes
        sc.pl.embedding(sp_adata, use_raw="counts",
                        basis="spatial", color=celltype,
                        color_map="jet", add_outline=True, ncols=1, ax=ax, vmin=0.1)

       
        


# ---- cell 3 ----
import pandas as pd
import scanpy as sc
import matplotlib as plt
import numpy as np
import seaborn as sns
from matplotlib.pyplot import rc_context
import anndata  
from matplotlib.colors import LinearSegmentedColormap


### load the excitatory anndata 

exc = sc.read_h5ad("path/Excitatory.h5ad")


#### gene signature for excitatory celltypes
match={
"Ex1":["LINC00507","SEMA3C",	"GNAL",	"SERPINE2",	"HPCAL1",	"THSD7A",	"MAML2",	"LAMP5"],
"Ex2":["CNGB1",	"GRIK1",	"LINC00326", "LRRC2",	"GRB14",	"PRKG2",		"LINC01478","LINC00470"],
"Ex3":["SV2C",	"GYG2",	"MFGE8",	"ENPEP",	"TEC",	"TXK",	"SYT2",	"GPAT3",	"ANKRD29",	"ONECUT2"],
"Ex4":["CCDC168",	"PRSS12",	"TEX30",	"ADAMTS6",	"CCDC68",	"PAH",	"CLMN",	"VIPR2",	"CALB1",	"RASSF3"],
"Ex5":["TRPC3",	"LAMA3",	"VAV3",		"NXPH1",	"IL2RA",	"PCAT1",	"EYA4",	"KCNIP1","KCNH8"],
"Ex6":["MME",	"COL22A1",	"CCDC168",	"GNG4",	"TEX30",	"BTNL9",	"ITGA11",	"GPR26",	"PHLDB2",	"SYT17"],
"Ex7":["LYPD6B",	"GABRG1",	"ANXA1",	"ALDH1A1",	"LOXHD1",	"PTK7",	"GOLIM4",	"VIPR2",	"ST8SIA4",	"MERTK"],
"Ex8":["MKX", "KCNK2",		"TMTC4",	"PTPRZ1",	"ARHGAP29",	"ASPM",	"CLMP",	"SFTPD",	"GPR161"], 
"Ex9":["PCP4","BTBD11",	"GPRIN3",		"KCNK2",			"MID1",	"PLD1"],
"Ex10":["CMTM8",	"MYBPC1",	"TYR",	"GRIN3A",	"NOX4",	"RNF182",	"TLL1",	"RBM20",	"ADTRP",	"CCDC68"],
"Ex11":["ADGRL4",	"NPFFR2",	"MEGF10",	"PKD2L1",	"LYPD6B",	"ARHGAP15",	"SULF2",	"RUNX2",	"SMIM36",	"ITGA11"],
"Ex12":["PRRX1",		"PXDN",	"MCUB",	"DCHS2",	"DKK2",			"ARHGAP18","LINC00343"],
"Ex13":["SMYD1",	"POSTN",	"OLFML2B",	"GAS2L3",	"SNTB1",	"MCTP2",	"NR4A2",	"PRLR",	"PDLIM5",	"KLHL1"],
"Ex14":["NXPH2",	"HTR2C",	"PDE9A",	"CARD11",	"KCNIP1",	"CD36",	"ERG",	"ITGA8",	"ROR1",	"ROBO3"],
"Ex15":["RREB1",	"ADRA1A",	"CACNA1H",	"RNF152",	"SLC5A8",	"POU3F1",	"ANGPT1",	"LRP2",	"PDE9A",	"ERG"],
"Ex16":["SYT6",	"SULF1",	"SH2D1B",	"SMIM36",	"SEMA5A",	"MCC",	"VAV2",	"ANKRD18A",	"ARHGAP6",	"CNTNAP3B"],
"Ex17":["RASEF",	"SEMA3D",	"NPFFR2",	"MCTP2",	"CDC14A",	"ITGA1",	"ITGA8",	"RNF220",	"RBM20",	"MDFIC"],
"Ex18":["SCUBE1",	"VCAN",	"CCN2",	"SLC15A5",	"FEZF2",	"SULF1",	"RNF220",	"VWA2",	"ERG",	"FAT4"]
}

for gs_name, gs_genes in match.items():
    exc.obs[gs_name] = exc[:, gs_genes].X.mean(axis=1)
    

# Define the colors for the custom colormap
colors = [(0.85, 0.85, 0.85), (0.545, 0.0, 0.545)]  # Light grey to magenta

# Define the positions for the colors in the colormap (0 to 1)
positions = [0.0, 2.0]

# Create the custom colormap using LinearSegmentedColormap
custom_cmap = LinearSegmentedColormap.from_list('custom_cmap', colors, N=256)

for gs_name, gs_genes in match.items():
    exc.obs[gs_name] = exc[:, gs_genes].X.mean(axis=1)

plt.rcParams.update({'font.size': 15})

fig = plt.figure(figsize=(15, 15))
sc.pl.umap(exc, size=2, color=list(match.keys())[0:18], cmap=custom_cmap, ncols=3, vmin=0.5,save="Ex_genesets.pdf")
plt.tight_layout()
plt.show()





# ---- cell 4 ----
import pandas as pd
import scanpy as sc
import matplotlib as plt
import numpy as np
import seaborn as sns
from matplotlib.pyplot import rc_context
import anndata  
from matplotlib.colors import LinearSegmentedColormap


### load the Inhibitory anndata 

inh = sc.read_h5ad("path/Inhibitory.h5ad")


match={
"In1":["PVALB",	"SULF1",	"DNAI1",	"HS3ST2",	"TAC1",	"TAFA4",	"HTR4",	"NEFH",	"RNF144B",	"CLMN"],
"In2":["MEPE",	"HGF",	"CPED1",	"LRMDA",	"PDGFC",	"PIEZO2",	"FGFR2",	"WIF1",	"COBLL1",	"AGBL1"],
"In3":["PLEKHH2",	"COL15A1",	"NOG",	"COL5A3",	"NPNT",	"MME",	"GSG1L",	"LDLRAD3",	"UNC5B",	"COL11A1"], 
"In4":["MSR1",	"SLC27A6",	"MAN1A1",	"FBN2",	"CALB1",	"DKK2",	"CRYBG3",	"CRACDL",	"ANOS1"],
"In5":["SLC17A8",	"SPON1",	"FBN2",	"ITGA1",	"KLHL1",	"SLC27A6",	"GABRG1",	"ADAMTS20",	"ILDR2",	"EPB41L4A"],
"In6":["EDNRA",	"SST",	"SLC9A2",	"RAB31",	"MAN1A1",	"UST",	"CRACDL",	"PIEZO2",	"PTPRU",	"MCUB"],
"In7":["EDNRA",	"SST",	"SPON1",	"TRPC6",	"B3GAT2",	"EPB41L4A",	"RAB31",	"CPNE4",	"MAN1A1"],
"In8":["TLL2",	"SEMA3A",	"EPB41L4A",	"WSCD1",	"SEL1L3",	"CRACDL",	"MRAP2",	"SST",	"NREP",	"PRKCG"],
"In9":["EVA1A",	"NPY",	"CORT",	"FAM163A",	"TENT5A",	"ANKRD34B",	"OTOF",	"CHODL",	"SST",	"COL24A1"],
"In10":["TMEM255A",	"HCRTR2",	"PDGFD",	"ARHGAP31",	"CA13",	"CA1",	"LAMP5",	"CA3",	"SFRP1",	"CHRDL1"],
"In11":["ARHGAP31",	"SOX13",	"TRPC3",	"KIT",	"ROR2",	"CA2",	"ETV1",	"ITGB5",	"PMEPA1"],
"In12":["NDNF",	"COL5A2",	"BMP6",	"SV2C",	"FAT1",	"DDR2",	"ATP2B4",	"DISC1"],
"In13":["SYT6",	"CDH23",	"ABCB5",	"ITGB8",	"PDLIM5",	"GABRG1",	"PBX3",	"DNAH11",	"DDR2",	"EYA1"],
"In14":["RXRG",	"SEMA3C",	"SMOC1",	"DISC1",	"ADAM33",	"NR2F2",	"GNG12",	"NCKAP5",	"TTN",	"MEGF11"],
"In15":["PTGFR",	"DACH2",	"SEMA3C",	"KCNJ2",	"PBX3",	"HTR2C",	"ADAMTSL1",	"KMO",	"MN1",	"MAML2"],
"In16":["TAC3",	"NRP1",	"RGS16",	"TSHZ2",	"KMO",	"IQGAP2",	"ADAM33",	"SLC22A3",	"PLPP4",	"RGS8"],
"In17":["SMOC1",	"PCP4",	"MCTP2",	"SLC22A3",	"IQGAP2",	"ARHGEF28",	"ABI3BP",	"CHRNA2",	"KANK1"],
"In18":["EXPH5",	"SHISA8",	"EMID1",	"SLC22A3",	"IGFBP5",	"TSHZ2",	"TBL1X",	"PXDN",	"CHD7",	"KMO"],
"In19":["NPR3",	"TNS3",	"CHRNA2",	"CALB2",	"COL11A1",	"ADAM33",	"ADRA1B",	"NCKAP5",	"IGFBP5",	"SCML4"]

}

for gs_name, gs_genes in match.items():
    inh.obs[gs_name] = inh[:, gs_genes].X.mean(axis=1)
    
# Define the colors for the custom colormap
colors = [(0.85, 0.85, 0.85), (0.545, 0.0, 0.545)]  # Light grey to magenta

# Define the positions for the colors in the colormap (0 to 1)
positions = [0.0, 2.0]

# Create the custom colormap using LinearSegmentedColormap
custom_cmap = LinearSegmentedColormap.from_list('custom_cmap', colors, N=256)

for gs_name, gs_genes in match.items():
    inh.obs[gs_name] = inh[:, gs_genes].X.mean(axis=1)

plt.rcParams.update({'font.size': 15})
fig = plt.figure(figsize=(15, 15), dpi=300)
sc.pl.umap(inh, size=2, color=list(match.keys())[0:19], cmap=custom_cmap, ncols=3, vmin=0.3,save="inh_genesets.pdf")


