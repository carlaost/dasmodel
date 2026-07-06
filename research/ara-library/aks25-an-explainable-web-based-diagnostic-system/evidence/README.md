# Evidence Index

> **Grounding: abstract-only — NO tables or figures were extracted.**
>
> The provided `paper.pdf` did NOT contain this paper. It is a different article: Afifi et al.,
> *Vision and convolutional transformers for Alzheimer's disease diagnosis: a systematic review*,
> Brain Informatics (2026) 13:1, DOI 10.1186/s40708-025-00286-7 (verified: 0 occurrences of
> "XRAI"/"Gradio"/"Aksoy"/"Daou"/"33,984"; 93 occurrences of "Afifi"; 92-page review). No licit OA
> copy of the target Aks25 article (Aksoy & Daou, Diagnostics, DOI 10.3390/diagnostics15202559)
> could be verified for this compile.
>
> Because no verified full text of the target paper was available, **the paper's own numbered
> tables and figures could not be enumerated or extracted.** Extracting the mismatched review's
> tables/figures and filing them under this paper's identity would be fabrication (Rule 2, Rule 8),
> so it was deliberately NOT done. **Evidence-completeness is N/A for this abstract-only compile.**
>
> The paper's quantitative claims (per its abstract) are captured in
> [`../logic/claims.md`](../logic/claims.md), each with a verbatim `**Sources**` quote from the
> abstract. The single verified data source is documented in
> [`../data/dataset.md`](../data/dataset.md).

## Tables

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| — | N/A (no full text available) | — | No tables extracted — see grounding note above. |

## Figures

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| — | N/A (no full text available) | — | No figures extracted — see grounding note above. |

## Numbers referenced by claims (abstract-sourced, not in an extracted table/figure)

These values are quoted verbatim from the paper's abstract (`metadata.json` / `metadata.md`), which
is the only verified text available. They are recorded here for traceability; they do not
correspond to an extracted evidence object because no full text was available.

| Value | Meaning | Claim | Verbatim abstract quote |
|-------|---------|-------|--------------------------|
| 99.18% | MobileNet-V3 accuracy, augmented test set | C01 | "MobileNet-V3 achieved the highest accuracy (99.18% on the augmented test set; 99.47% on the original dataset)" |
| 99.47% | MobileNet-V3 accuracy, original dataset | C01 | "(99.18% on the augmented test set; 99.47% on the original dataset)" |
| 4.2M | MobileNet-V3 parameter count | C02 | "while using the fewest parameters (4.2M)" |
| 33,984 | Augmented dataset image count | C01, C02 | "an augmented Kaggle dataset (33,984 images across four AD severity classes)" |
| sub-20 s | Web interface inference latency | C04 | "The web interface delivered sub-20 second inference" |
