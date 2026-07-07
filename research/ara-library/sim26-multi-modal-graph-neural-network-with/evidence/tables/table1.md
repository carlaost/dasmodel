# Table 1: Preclinical AD classification performance (CN/SMC/EMCI) on ADNI data

- **Source**: Table 1, §3 (Experiments — Classification Result)
- **Caption**: "Preclinical AD classification performance (CN/SMC/EMCI) on ADNI data."
- **Screenshot**: table1.png
- **Extraction type**: raw_table

All values are mean ± standard deviation over 5-fold cross-validation. Bolded rows in the source
(GTAD (Ours), shaded) are marked here in the **Method** column.

## Modalities: Cortical Thickness & β-Amyloid

| Method | Accuracy | Precision | Recall |
|---|---|---|---|
| GCN [12] | 0.861±0.04 | 0.772±0.06 | 0.780±0.06 |
| GAT [22] | 0.896±0.01 | 0.827±0.03 | 0.839±0.02 |
| GraphHeat [26] | 0.868±0.02 | 0.777±0.05 | 0.797±0.04 |
| GDC [7] | 0.858±0.02 | 0.767±0.03 | 0.786±0.04 |
| ADC [27] | 0.906±0.02 | 0.835±0.03 | 0.861±0.04 |
| LSAP [18] | 0.911±0.01 | 0.847±0.03 | 0.872±0.02 |
| NodeFormer [24] | 0.916±0.02 | 0.856±0.04 | 0.865±0.02 |
| DIFFormer [23] | 0.930±0.01 | 0.877±0.03 | 0.900±0.02 |
| SGFormer [25] | 0.941±0.01 | 0.894±0.03 | 0.911±0.02 |
| **GTAD (Ours)** | **0.945±0.02** | **0.901±0.03** | **0.919±0.02** |

## Modalities: Cortical Thickness & FDG

| Method | Accuracy | Precision | Recall |
|---|---|---|---|
| GCN [12] | 0.873±0.02 | 0.802±0.02 | 0.813±0.03 |
| GAT [22] | 0.882±0.02 | 0.811±0.03 | 0.844±0.03 |
| GraphHeat [26] | 0.887±0.03 | 0.821±0.04 | 0.834±0.03 |
| GDC [7] | 0.842±0.01 | 0.743±0.02 | 0.765±0.03 |
| ADC [27] | 0.896±0.01 | 0.831±0.01 | 0.847±0.02 |
| LSAP [18] | 0.934±0.02 | 0.899±0.05 | 0.904±0.03 |
| NodeFormer [24] | 0.944±0.01 | 0.913±0.03 | 0.921±0.02 |
| DIFFormer [23] | 0.954±0.01 | 0.923±0.02 | 0.944±0.01 |
| SGFormer [25] | 0.959±0.01 | 0.931±0.01 | 0.945±0.01 |
| **GTAD (Ours)** | **0.963±0.01** | **0.935±0.02** | **0.948±0.01** |

## Modalities: β-Amyloid & FDG

| Method | Accuracy | Precision | Recall |
|---|---|---|---|
| GCN [12] | 0.880±0.01 | 0.806±0.02 | 0.813±0.02 |
| GAT [22] | 0.877±0.02 | 0.815±0.03 | 0.814±0.04 |
| GraphHeat [26] | 0.880±0.02 | 0.804±0.05 | 0.824±0.03 |
| GDC [7] | 0.866±0.02 | 0.787±0.03 | 0.790±0.03 |
| ADC [27] | 0.910±0.01 | 0.865±0.02 | 0.856±0.02 |
| LSAP [18] | 0.922±0.02 | 0.862±0.05 | 0.893±0.03 |
| NodeFormer [24] | 0.931±0.01 | 0.887±0.03 | 0.893±0.03 |
| DIFFormer [23] | 0.951±0.01 | 0.919±0.03 | 0.933±0.02 |
| SGFormer [25] | 0.954±0.01 | 0.923±0.03 | 0.936±0.02 |
| **GTAD (Ours)** | **0.962±0.01** | **0.935±0.02** | **0.946±0.02** |

## Modalities: All Imaging Features

| Method | Accuracy | Precision | Recall |
|---|---|---|---|
| GCN [12] | 0.888±0.02 | 0.816±0.02 | 0.826±0.02 |
| GAT [22] | 0.912±0.01 | 0.858±0.02 | 0.864±0.02 |
| GraphHeat [26] | 0.893±0.02 | 0.824±0.03 | 0.839±0.03 |
| GDC [7] | 0.867±0.02 | 0.779±0.03 | 0.799±0.02 |
| ADC [27] | 0.904±0.02 | 0.855±0.04 | 0.858±0.02 |
| LSAP [18] | 0.912±0.01 | 0.844±0.04 | 0.879±0.02 |
| NodeFormer [24] | 0.938±0.02 | 0.900±0.03 | 0.902±0.03 |
| DIFFormer [23] | 0.953±0.01 | 0.920±0.02 | 0.936±0.02 |
| SGFormer [25] | 0.951±0.01 | 0.911±0.02 | 0.933±0.02 |
| **GTAD (Ours)** | **0.963±0.01** | **0.943±0.01** | **0.941±0.02** |
