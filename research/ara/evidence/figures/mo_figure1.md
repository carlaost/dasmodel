# Figure 1: Processed reaction interaction network of cholesterol biosynthesis
- **Source**: Figure 1, Section "Fingerprints in biological Networks" / "Data Preparation" (p. 2317)
- **Caption**: "Processed reaction interaction network of cholesterol biosynthesis"
- **Screenshot**: mo_figure1.png
- **Figure type**: diagram
- **Extraction method**: visual_description
- **Reading confidence**: high

## Visual description
- **Components**: Blue circular nodes, each labelled with an enzyme/reaction name from the
  cholesterol biosynthesis pathway. Readable labels include: "4alpha-methyl... monooxygenase",
  "...3beta-... (decarboxylating)", "DELTA... -desaturase", "plant 3beta-hydroxysteroid-4alpha-carb...",
  "3beta-hydroxysteroid dehydrogenase", "DELTA(24)... reductase", "Cycloeucalenol cycloisomerase",
  "sterol 14alpha-demethylase", "7-dehydrocholesterol reductase", "cholesterol DELTA-isomerase",
  "DELTA14-sterol reductase", "3beta-hydroxysteroid 3-dehydrogenase",
  "plant 3beta-hydroxysteroid-4alpha-carboxylate 3-dehydrogenase (decarboxylating)".
- **Connections**: Directed edges (arrows) drawn between nodes, forming a densely connected
  graph (near-clique). Edges represent possible subsequent interactions / successor reactions
  in the pathway space (a reaction's product being a substrate of another reaction).
- **Annotations**: All nodes are the same blue color (no omics-type coloring at this stage);
  this is the raw processed interaction graph before embedding, not the embedded space.
- **What it conveys**: Illustrates the "complex interaction network found in biological systems"
  that motivates the method — a single pathway (cholesterol biosynthesis) already yields a dense
  web of reaction-to-reaction relations. This is the graph from which interaction chains are
  sampled (random reaction start, walk to successors until sequence_length is reached).
