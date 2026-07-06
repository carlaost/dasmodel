# Unnumbered Figure: Epoch-wise evolution of attention heatmaps during model fine-tuning

- **Source**: Unnumbered illustrative figure, §"Transformer and hybrid attention models" (image on PDF p.631; caption text on p.632)
- **Caption**: "Examples of Epoch-Wise Evolution of Attention Heatmaps During Model Fine-Tuning. This figure shows the progression of model attention maps across multiple training epochs, beginning with the original MRI image and the initial attention map before fine-tuning, followed by updated heatmaps from Epoch 1 through Epoch 10. The sequence illustrates how the model's focus changes during training and how the highlighted regions gradually become more concentrated on diagnostically relevant image areas. Warmer colors indicate stronger model attention, while cooler colors represent lower contribution."
- **Screenshot**: figure_unnum_attention.png
- **Figure type**: qualitative_sample
- **Extraction method**: visual_description
- **Reading confidence**: medium

## Visual description
- **Shows**: A grid of ~5 rows × 12 columns. Column 1 = original grayscale brain MRI slice; column 2 =
  "Before fine-tuning" attention map; columns 3-12 = attention heatmaps at "Epoch 1" through "Epoch 10".
  Warm colors (red/yellow) mark stronger attention on a blue background.
- **Demonstrates**: How attention/heatmap focus concentrates on diagnostically relevant regions over
  fine-tuning epochs — an interpretability illustration for attention-based models.
- **Supports**: C05 (explainability via visualization) and concept "Transformer / self-attention".
- **Note**: This figure carries **no figure number** in the source (illustrative). It is filed here for
  completeness and accounted for in evidence/README.md.
