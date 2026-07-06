# Figure 4: Resulting embedding space after running the embedding model
- **Source**: Figure 4 (panels a–d), Section "RESULTS" (p. 2319)
- **Caption**: "Resulting embedding space after running the embedding model"
- **Screenshot**: mo_figure4.png
- **Figure type**: mixed (4 panels: 2 t-SNE scatter, 1 scatter/index plot, 1 histogram)
- **Extraction method**: digitized_estimate / visual_description
- **Reading confidence**: medium (panels a–c dense scatter; panel d histogram readable)

This is a 4-panel figure. Each panel is described/read separately below.

---

## Panel a) — "t-SNE Visualization of molecules with clustering"
- **Plot kind**: scatter (2-D t-SNE), points colored by cluster ID
- **Axes**: X = t-SNE Component 1 (unitless, linear, range ≈ -30 to 40),
  Y = t-SNE Component 2 (unitless, linear, range ≈ -40 to 35)
- **Extraction method**: visual_description (cluster colors are categorical, not numeric)

### Visual description
Points form several distinct, dense "islands"/blobs colored by cluster assignment (a clustering
algorithm was run on the embedding). Multiple separable clusters are visible (greens, teals,
dark purples, and a distinct yellow cluster in the lower-right ≈ (25 to 35, -20 to -10)).
Clusters are spatially separated rather than uniformly mixed.

### Trend summary
The embedding produces visibly separable clusters — qualitative support that related pathway
nodes form distinct islands. The discrete yellow cluster in the lower right is the most clearly
isolated. Exact cluster count not labelled.

---

## Panel b) — "t-SNE Visualization of molecules with omic type"
- **Plot kind**: scatter (same t-SNE layout as panel a), points colored by omics type
- **Axes**: X = t-SNE Component 1 (linear, ≈ -30 to 40), Y = t-SNE Component 2 (linear, ≈ -40 to 35)
- **Legend (exact)**: metabolites (dark purple), enzymes (teal), genes (yellow)
- **Extraction method**: visual_description

### Visual description
The same point cloud as panel a, now colored by the three omics modalities. Metabolites (purple)
dominate overall; genes (yellow) and enzymes (teal) are distributed throughout. The paper states
"different pathway modalities are well distributed in the space despite genes being less abundant
in the left half." All three modalities co-occur within clusters rather than segregating into
modality-only regions.

### Trend summary
Modalities are interspersed within shared clusters (genes, proteins/enzymes, small molecules sit
near each other) — the central claim that the space unifies omics types into one shared geometry,
not separate per-modality regions.

---

## Panel c) — "Most similar word index for each word"
- **Plot kind**: scatter / index map
- **Axes**: X = Word index (count, linear, ≈ 0 to ~23000),
  Y = Most similar word index (count, linear, ≈ 0 to ~23000)
- **Extraction method**: visual_description

### Visual description
A scatter of, for each node ("word"), the index of its most-similar node. Background points are
near-uniform random noise, with several overlaid linear features: a main diagonal segment, a
horizontal band at Y ≈ 8000–9000, and additional shorter diagonal/anti-diagonal streaks. The
paper explains the apparent diagonal arises because nodes are implicitly ordered as pathways are
processed, so similar indices ⇒ higher likelihood of being in the same pathway; "The diagonal has
been set to zero" (self-matches excluded). The total node count is on the order of ~23,000.

### Trend summary
Most-similar-node relationships are non-random and correlate with pathway-derived index proximity
(diagonal/band structure), evidence the embedding preserves pathway-local structure rather than
producing random nearest neighbors.

---

## Panel d) — "Dot Product Distribution"
- **Plot kind**: histogram
- **Axes**: X = Dot Product (unitless, linear, ≈ -100 to ~130),
  Y = Frequency (count, linear; Y axis scaled by 1e8, peak ≈ 2.9e8)
- **Extraction method**: digitized_estimate

### Reading (approximate)
| Dot Product (X) | Frequency (≈, ×1e8) |
|-----------------|---------------------|
| ≈ -75 to -25    | ≈ 0.2 (low, wide tail) |
| ≈ 0 (sharp peak)| ≈ 2.9 (tallest bar) |
| ≈ 25 to 100     | ≈ 0.3–0.5 (broad shoulder, decaying) |

### Trend summary
The dot-product distribution between all embeddings has the shape of a mixture of two
distributions: a sharp narrow peak centered near 0 (the paper attributes this to unrelated /
non-interacting node pairs) and a smaller, wider/broader distribution (related node pairs). The
broad right shoulder (positive dot products up to ≈ 100+) corresponds to related pairs with a
"smaller but wider peak." This bimodal/mixture shape is the quantitative evidence that related
and unrelated pairs are separated by the learned alignment objective.
