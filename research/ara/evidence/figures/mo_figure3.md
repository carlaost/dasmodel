# Figure 3: Embedding Model Objective Schematic
- **Source**: Figure 3, Section "Embedding Model" (p. 2318)
- **Caption**: "Embedding Model Objective Schematic"
- **Screenshot**: mo_figure3.png
- **Figure type**: diagram
- **Extraction method**: visual_description
- **Reading confidence**: high

## Visual description
- **Components**: Three vertical columns of colored circles:
  - Left column labelled "Token": four yellow nodes containing the values 0, 1, 0, "." (a
    one-hot-style encoded target node vector).
  - Middle column: three orange/red nodes containing 1, 0, 1 (the compressed lower-dimensional
    embedding representation).
  - Right column labelled "Context": four green nodes containing 1, 0, 1, "." (the
    reconstructed / predicted context one-hot vector).
- **Connections**: Dotted lines fan from each left (Token) node to the middle (embedding) nodes,
  and from the middle nodes out to each right (Context) node — a fully connected
  encode-then-decode / target→embedding→context mapping.
- **Annotations**: Color encodes role: yellow = input token one-hot, orange = compressed
  embedding, green = predicted context one-hot. The crossing dotted edges depict the dense
  linear projection (no per-edge weights shown).
- **What it conveys**: The training objective — compress a one-hot target ("Token") into a
  lower-dimensional embedding, then use it to predict its pathway-context node ("Context"). The
  alignment of related (positive) target/context pairs and misalignment of unrelated (negative)
  pairs is what the embedding learns. Conceptually mirrors a Word2Vec skip-gram /
  autoencoder-style objective over pathway nodes.
