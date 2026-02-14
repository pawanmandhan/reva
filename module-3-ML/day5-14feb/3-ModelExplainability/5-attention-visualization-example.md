Great 🔥 Let’s see a **simple attention visualization example** using a Transformer (like BERT).

We’ll:

1. Load a pretrained model
2. Enable attention output
3. Extract attention weights
4. Visualize them as a heatmap

---

# 🧠 What We Are Visualizing

Attention formula:

[
Attention(Q,K,V) = softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V
]

The important part:

[
softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)
]

This gives **attention weights**
→ How much each token attends to other tokens.

---

# ✅ Example: Visualizing Attention in BERT

```python
# Install if needed:
# pip install transformers torch seaborn matplotlib

import torch
import seaborn as sns
import matplotlib.pyplot as plt
from transformers import BertTokenizer, BertModel

# Load pretrained BERT model with attention output enabled
model = BertModel.from_pretrained(
    "bert-base-uncased",
    output_attentions=True
)

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Example sentence
sentence = "The movie was great but the ending was bad"

# Tokenize input
inputs = tokenizer(sentence, return_tensors="pt")

# Forward pass
outputs = model(**inputs)

# Get attention weights
# Shape: (layers, batch, heads, seq_len, seq_len)
attentions = outputs.attentions

# Select:
# Layer 0
# Head 0
attention_matrix = attentions[0][0][0].detach().numpy()

# Get token labels
tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

# Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(attention_matrix,
            xticklabels=tokens,
            yticklabels=tokens,
            cmap="viridis")

plt.title("Attention Heatmap (Layer 1, Head 1)")
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.show()
```

---

# 📊 What This Shows

Each row = Query token
Each column = Key token

If row “bad” has high weight on column “ending”,
it means:

> “bad” attends strongly to “ending”.

---

# 🧠 How to Explain in Interview

> Attention visualization shows how strongly each token interacts with every other token in a sentence. It helps interpret which words influence a prediction in Transformer models.

---

# 🔥 Advanced Options

You can also:

* Average across heads
* Average across layers
* Visualize only CLS token attention
* Use attention rollout

Example (average across heads):

```python
attention_avg = attentions[0][0].mean(dim=0).detach().numpy()
```

---

# 🎯 Key Insight

CNN explanation → Where in image?
Transformer explanation → Who influences who?

Attention heatmaps reveal relational reasoning.

---

If you want, I can next show:

* CLS token classification attention
* Vision Transformer attention visualization
* Attention rollout method
* Real sentiment classification example

Just tell me 🚀
