# Figure 2: Embedding Model
- **Source**: Figure 2, Section "Embedding Model" (p. 2318)
- **Caption**: "Embedding Model"
- **Screenshot**: mo_figure2.png
- **Figure type**: diagram
- **Extraction method**: visual_description
- **Reading confidence**: high

## Visual description
This figure is a verbatim pseudocode listing (not a plot). Transcription:

```
class BioEmbeddingModel
  function INIT (vocab_size, embed_dim)
      target_embedding  ← Linear(vocab_size, embed_dim)
      context_embedding ← Linear(vocab_size, embed_dim)
      activation function ← TANH
  function FORWARD (input, context)
      target_embeddings  ← target_embedding(input)
      context_embeddings ← context_embedding(context)
      target_embeddings  ← tanh(target_embeddings)
      context_embeddings ← tanh(context_embeddings)
      return DOTS(target_embeddings, context_embeddings)
  function GetWordEmbedding (word)
      embedding ← target_embedding(word)
      return tanh(embedding)
```

- **Components**: A class `BioEmbeddingModel` with two separate linear embedding layers
  (`target_embedding`, `context_embedding`), each mapping `vocab_size` → `embed_dim`, a `tanh`
  activation, a `FORWARD` that returns the dot product of (tanh-activated) target and context
  embeddings, and a `GetWordEmbedding` retrieval method returning the tanh of the target embedding.
- **Connections**: input → target_embedding → tanh; context → context_embedding → tanh; the two
  branches meet at a dot product (`DOTS`) that produces the prediction compared against the
  learning_target in the loss.
- **What it conveys**: The model is a shallow (single linear layer per branch) Word2Vec-style
  two-tower (target/context) embedding network with separate target and context projection
  matrices and a tanh nonlinearity; the trained node embedding is the tanh of the target layer.
