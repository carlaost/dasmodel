# Algorithm — Loss Formulations

All equations transcribed from §3.3–§3.6 and verified against the rendered pages (the raw PDF text
contains OCR artifacts such as duplicated `log log` / `exp exp`; the clean forms below are read from
the rendered equations). Equation numbers match the paper.

## SSL pretraining objectives (§3.3)

**Eq. 1 — Intra-modal InfoNCE**
$$\mathcal{L}_{intra} = -\sum_{i\in B}\log\frac{\exp\!\big(\text{sim}(z_i,z_i^+)/\tau\big)}{\sum_{j\in B\cup M\setminus\{i\}}\exp\!\big(\text{sim}(z_i,z_j)/\tau\big)}$$
$B$ = batch of paired views; $M$ = optional MoCo queue of negatives; $z_i^+$ = positive (other augmented view).

**Eq. 2 — Cross-modal symmetric InfoNCE** (MRI and PET alternate as anchors)
$$\mathcal{L}_{cross} = -\sum_{i\in B}\log\frac{\exp\!\big(\text{sim}(z^{MRI}_i,z^{PET}_i)/\tau\big)}{\sum_{j\in B\cup M}\exp\!\big(\text{sim}(z^{MRI}_i,z^{PET}_j)/\tau\big)} \;-\; \sum_{i\in B}\log\frac{\exp\!\big(\text{sim}(z^{PET}_i,z^{MRI}_i)/\tau\big)}{\sum_{j\in B\cup M}\exp\!\big(\text{sim}(z^{PET}_i,z^{MRI}_j)/\tau\big)}$$

**Eq. 3 — Longitudinal consistency** (within modality)
$$\mathcal{L}_{long} = \sum_p\sum_{\substack{t_1,t_2\in T_p\\ t_1\neq t_2}}\lVert z^m_{p,t_1}-z^m_{p,t_2}\rVert_2^2,\quad m\in\{MRI,PET\}$$

**Eq. 4 — Optional cross-time cross-modal coupling** (enabled only where longitudinal MRI and PET co-exist)
$$\mathcal{L}_{long\_x} = \sum_p\sum_{t_1,t_2\in T_p}\lVert z^m_{p,t_1}-z^m_{p,t_2}\rVert_2^2$$

**Eq. 5 — BYOL-style regression** (predictor $q_\omega$, stop-gradient target)
$$\mathcal{L}_{byol} = \sum_{i\in B}\lVert q_\omega(z_i)-\text{sg}(z_i^+)\rVert_2^2$$

**Eq. 6 — Domain-adversarial site invariance** (discriminator $D_\psi$ via GRL)
$$\mathcal{L}_{site} = \mathbb{E}\big[\text{CE}(D_\psi(z),s_p)\big]$$

**Eq. 7 — Total SSL objective**
$$\mathcal{L}_{SSL} = \lambda_1\mathcal{L}_{intra}+\lambda_2\mathcal{L}_{cross}+\lambda_3\mathcal{L}_{byol}+\lambda_4\mathcal{L}_{long}+\lambda_5\mathcal{L}_{long\_x}+\lambda_3\mathcal{L}_{site}$$
(Verbatim: $\lambda_3$ appears on both $\mathcal{L}_{byol}$ and $\mathcal{L}_{site}$; $\lambda$ values are "Not specified in paper".)

## Fine-tuning objectives (§3.4)

**Eq. 8 — Gating fusion**: $\alpha=\sigma(w^\top[\mathbb{1}_{MRI},\mathbb{1}_{PET}])\in[0,1]$; $\;e=[\alpha z^{MRI}\Vert(1-\alpha)z^{PET}\Vert c]$

**Eq. 9 — Class-weighted cross-entropy diagnosis loss**
$$\mathcal{L}_{diag} = -\frac{1}{N}\sum_{n=1}^{N}\sum_{k=0}^{K-1} w_k\,\mathbb{1}\{y_n=k\}\,\log\frac{\exp(l_{n,k})}{\sum_{k'}\exp(l_{n,k'})}$$

**Eq. 10 — Cox partial log-likelihood (survival head $r_\varphi$)**
$$\mathcal{L}_{cox} = -\sum_{n:\delta_n=1}\Big(r_n-\log\sum_{j\in R(T_n)} e^{r_j}\Big),\quad R(T_n)=\{j:T_j\ge T_n\}$$

**Eq. 11 — PET→MRI distillation** (training only, subjects with PET)
$$\mathcal{L}_{distill} = \frac{1}{N}\sum_n \mathbb{1}_{PET,n}\,\lVert z^{MRI}_n-\text{sg}(z^{PET}_n)\rVert_2^2$$

**Eq. 12 — Temperature scaling** (post-hoc calibration, $T>0$)
$$\mathcal{L}_{cal} = -\frac{1}{N}\sum_n\log\frac{\exp(l_{n,y_n}/T)}{\sum_k\exp(l_{n,k}/T)}$$

**Eq. 13 — Joint fine-tuning objective**
$$\mathcal{L}_{FT} = \alpha\,\mathcal{L}_{diag}+\beta\,\mathcal{L}_{cox}+\gamma\,\mathcal{L}_{distill},\quad \alpha,\beta,\gamma\ge 0$$

## Metrics (§3.6)

**Eq. 14 — Balanced accuracy**: $\text{BAC}=\tfrac12(\text{TPR}+\text{TNR})$, $\text{TPR}=\tfrac{TP}{TP+FN}$, $\text{TNR}=\tfrac{TN}{TN+FP}$

**Eq. 15 — Harrell's C-index**: $C=\tfrac{1}{|P|}\sum_{(i,j)\in P}\mathbb{1}[(T_i<T_j)\wedge(r_i>r_j)]$, $P=\{(i,j):\delta_i=1,T_i<T_j\}$

**Eq. 16 — Integrated Brier score**: $\text{IBS}=\tfrac{1}{\tau}\int_0^\tau \text{Brier}(t)\,dt$ (with IPCW)

**Eq. 17 — Expected calibration error**: $\text{ECE}=\sum_{m=1}^{M}\tfrac{|B_m|}{N}\,|\text{acc}(B_m)-\text{conf}(B_m)|$ ($M$ equal-mass bins)

## Procedure (§3.7)
1. SSL-pretrain on unlabeled MRI±PET from ADNI, OASIS-3 (and AIBL/BioFINDER when licensing permits), optimizing Eq. 7. $\mathcal{L}_{long}$ (Eq. 3) enabled only where repeat visits exist; $\mathcal{L}_{long\_x}$ (Eq. 4) only when longitudinal MRI and PET co-exist (typically ADNI).
2. Linear probes select the best SSL checkpoint on a held-out validation fold.
3. Initialize encoders with the checkpoint; fine-tune with Eq. 13; gating (Eq. 8) handles missing modalities; Eq. 11 transfers PET knowledge to MRI.
4. Fit temperature $T$ on validation predictions (Eq. 12).
5. Evaluate: in-distribution site-stratified 5-fold CV; OOD ADNI↔OASIS-3 (+AIBL/BioFINDER external); MIRIAD reserved for reliability.

## Complexity
Not specified in paper.
