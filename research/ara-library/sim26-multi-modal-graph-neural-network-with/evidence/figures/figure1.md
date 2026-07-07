# Figure 1: Illustration of GTAD

- **Source**: Figure 1, §2 (Method)
- **Caption**: "Illustration of GTAD. A graph (as L̂) and node feature x^m are inputted to m-th
  encoder at the adaptive convolution block. Then, all outputs {H^m_Z}_{m=1}^{M} from this block
  are inputted to the self-attention block, producing an output B_P. Finally, the B_P is entered
  into a classifier f_R which yields a prediction Ŷ. To adaptively adjust the node-wise scales for
  each modality, the loss L from Ŷ is backpropagated to update m-th encoder with scales s^m."
- **Screenshot**: figure1.png
- **Figure type**: diagram
- **Extraction method**: visual_description
- **Reading confidence**: high

## Visual description

- **Components** (left to right):
  - **Graph Input**: a small icon of a node-and-edge graph with color-coded node features.
  - **Per-modality branch (×M)**: for each modality `m`, an "Initial `s^m`" graph icon (showing a
    node-wise scale, visualized as colored dots on a small graph), combined ("+") with a
    "Feature `x^m`" / "Laplacian `L̂`" pair, feeding into an **Adaptive Convolution Block** (labeled
    "×Z", containing "Adaptive Convolution `e^{-s^m L̂} H^m_{z-1} W^m_z`" → "Activation Function
    `σ_z`") that outputs `H^m_Z` (drawn as a colored vertical bar, one per modality: `H^1_Z` red,
    `H^M_Z` green in the rendered figure).
  - **Self-Attention Block** (labeled "×P"): receives all `{H^m_Z}` bars; internally shows
    per-modality `Q^m, K^m, V^m` blocks (color-coded red/green/teal boxes stacked "M" deep) feeding
    "Multi-Head Self-Attention" → "Add & Norm" → "Feed-Forward Network" → "Add & Norm", producing
    output `B_P` (grey bar).
  - **Classifier `f_R`**: takes `B_P`, outputs prediction `Ŷ` ("Label").
  - **Loss `L`**: computed from `Ŷ` (and the true label), shown at the far right.
  - **Scale Update path**: a dashed/dotted line runs from the Loss `L` box back to each modality's
    "Scale (`s^m`) Update" annotation next to the Initial `s^m` boxes, looping around the top and
    bottom of the figure — visually representing backpropagation from the loss into the per-modality
    scale parameters.

- **Connections** (data flow):
  Graph Input → {Feature `x^m`, Laplacian `L̂`} (per modality, ×M in parallel) + Initial `s^m` →
  Adaptive Convolution Block (×Z layers) → `H^m_Z` → Self-Attention Block (×P layers, using
  `{H^m_Z}` as Q/K/V for the first layer) → `B_P` → Classifier `f_R` → `Ŷ` → Loss `L` →
  (backprop, dotted arrows) → Scale (`s^m`) Update for each modality's encoder.

- **Annotations**: Blue-shaded boxes group the "Adaptive Convolution Block" and "Self-Attention
  Block" as the two named architectural stages. Small graph icons with colored nodes (yellow →
  orange → red gradient) inside the "Scale Update" strips visually suggest the scale value at each
  node changing color/magnitude as it updates during training.

- **What it conveys**: The figure conveys GTAD's two-stage, per-modality-parallel-then-fused
  architecture (see `logic/solution/architecture.md` for the corresponding component breakdown),
  and specifically that the node-wise scale parameters `s^m` are not fixed inputs but are updated
  end-to-end via the loss gradient — the closed loop drawn from `L` back to "Scale Update" is the
  figure's key structural claim (mirrored in Eq. 7's `s ← s − β ∂L/∂s`).
