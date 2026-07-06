# Non-code Artifacts

Concrete deliverables released with the study that have no capturable plain-text source
(binary/XML pipelines, pretrained model archives, biological reagents). Runnable code files are
captured separately in `src/execution/`.

## CellProfiler image-analysis pipelines
- **File(s) in repo**: `EYA4 KCNIP4 analysis L4.cpproj`, `EYA4 KCNIP4 analysis L2.cpproj`, `GFP KCNIP4 analysis cfos.cpproj`, `GFP KCNIP4 analysis arc.cpproj` (AkilaRanjith/…-Neocortical-Layer-4-Neurons)
- **Nature**: CellProfiler project files (`.cpproj`, binary/XML), ~75–81 KB each.
- **What it does / contains**: Custom automated segmentation of NeuN+ neurons and, for mouse, GFP+/GFP− neurons; measurement of KCNIP4 soma intensity in human L4 EYA4+ / L2/3 neurons; quantification of c-Fos+ proportion and Arc mean intensity in mouse cortex.
- **How to use / run**: Open in CellProfiler; apply to confocal images (Zeiss LSM980).
- **Claims supported**: C06 (human KCNIP4 intensity), C08 (mouse c-Fos / Arc).

## Pretrained cell-type prediction models
- **File(s) in repo**: `exc_pretrain.zip` (~17.6 MB), `inh_pretrain.zip` (~17.0 MB); loaded via `pretrained_model.ipynb` → captured as `execution/pretrained_model.py`.
- **Nature**: Serialized scANVI-based model archives for excitatory / inhibitory neuronal subtype prediction.
- **What it does / contains**: Predict this study's 18 Ex / 19 In cluster labels on new/query snRNA-seq data.
- **How to use / run**: See `execution/pretrained_model.py` (load model, transfer labels).
- **Claims supported**: C10 (cross-dataset applicability).

## AAV vectors (biological reagents)
- **File(s) in repo**: n/a (physical reagents; sequences referenced by NCBI/Addgene ID).
- **Nature**: Recombinant AAV expression constructs.
- **What it does / contains**:
  - `PHP.eB-CaMKIIa-Kcnip4-P2A-EGFP` — excitatory-neuron-targeted mouse Kcnip4 (isoform 1; NP_001186171.1) overexpression with EGFP reporter (Vector Biolabs).
  - `PHP.eB-CaMKIIa-EGFP` — control (Addgene #50469-PHPeB).
  - `PHP.eB-Syn.NES-jRGECO1a.WPRE.SV40` — calcium indicator (Addgene #100854-PHPeB).
- **How to use / run**: MOI 5000 vg/cell in vitro; 1×10¹¹ vg retro-orbital in vivo.
- **Claims supported**: C07, C08.

## Deposited datasets
See `data/dataset.md` and `logic/related_work.md` for GEO/CELLxGENE/Zenodo accessions.
