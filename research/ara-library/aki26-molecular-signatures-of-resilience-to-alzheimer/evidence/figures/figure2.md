# Figure 2: Layer-specific localization of excitatory neuronal subtypes in BA9 and BA17 by Xenium
- **Source**: Figure 2, §"Spatial distribution of neuronal cell types in association (BA9) vs primary (BA17) cortices"
- **Caption**: "a Experimental design for spatial single-cell analysis… using Xenium. A representative Xenium slide (slide 2) with four tissue sections (AD-BA17, AD-BA9, Ctrl-BA17, Ctrl-BA9)… b UMAP and bar plots depicting the relative abundance of major cell types in the Xenium dataset (765,992 cells, after QC), and representative spatial maps of BA9 and BA17… c Spatial maps of the annotated 18 excitatory clusters across all 16 sections… d Representative spatial maps after segmentation and annotation… at the cell subclass level… e Representative cortex from control BA9 and BA17 sections showing staining with DAPI, ribosomal RNA, and αSMA/Vimentin… f Spatial maps for each excitatory cluster… within L2/3, L4, L5, and L6."
- **Screenshot**: figure2.png
- **Figure type**: mixed (diagram/workflow + qualitative spatial maps + quantitative relative-fraction bar)
- **Extraction method**: exact_from_labels (text-stated) + visual_description
- **Reading confidence**: high (design/labels); medium (spatial density)

## Visual description
- **Panel a (diagram)**: 4 slides / 16 sections (8 BA9, 8 BA17; 4 AD, 4 control); Xenium workflow: staining & hybridization (266-gene panel + 100-gene custom + cell-segmentation add-on) → Xenium Ranger → cell segmentation → major-cell-type annotation (canonical markers, ingest transfer, spatialID) → neuronal subtype annotation (ingest from snRNA-seq).
- **Panel b (UMAP + bar + spatial)**: 765,992 cells; major-cell-type relative fraction; spatial maps of BA9 vs BA17 (higher neuronal density in BA17).
- **Panel c (spatial maps)**: 18 excitatory clusters across all 16 sections; BA9 vs BA17 differences; small BA18 areas excluded.
- **Panel d (spatial maps)**: subclass-level layer annotation (L2/3 IT, L4 IT, L5 IT/ET, L5/6 NP, L6 IT/CT, L6 IT Car3, L6b); dashed lines = layer boundaries; L4 ~>1/3 of cortex in BA17 vs <10% in BA9.
- **Panel e (micrograph)**: control BA9 & BA17 with DAPI / ribosomal RNA / αSMA-Vimentin stains and multimodal cell-segmentation boundaries.
- **Panel f (spatial maps)**: per-cluster layer overlays; L2/3 = Ex1–Ex4; L4 = Ex5–Ex7; L5 = Ex8–Ex11, Ex14, Ex15; L6 = Ex12, Ex13, Ex16–Ex18. Ex5 overrepresented BA17; Ex6/Ex7 overrepresented BA9.

## Key text-stated quantities
| Quantity | Value |
|----------|-------|
| Xenium cells after QC | 765,992 |
| Sections | 16 (8 BA9, 8 BA17) |
| Donors | 4 AD + 4 control |
| L4 thickness | ~>1/3 cortex in BA17; <10% in BA9 |

## Trend / structural summary
Spatially confirms the snRNA-seq taxonomy and the region-specific L4 composition (Ex5 BA17-enriched;
Ex6/Ex7 BA9-enriched). Supports C01, C10.
