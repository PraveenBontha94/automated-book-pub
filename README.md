 # Automated Book Versioning and Retrieval

This project demonstrates how to store, semantically search, and rank multiple versions of book chapters using [ChromaDB](https://docs.trychroma.com/) and a simple RL-style reward scoring system.

---

## Objective

Given a single chapter of a book in multiple stages:
- `raw` (original scrape)
- `writer` (AI-written version)
- `reviewer` (AI-reviewed version)
- `final` (human-edited version)

This project:
1. Stores each version in ChromaDB with metadata.
2. Allows **semantic search** across all versions using embeddings.
3. Ranks and returns the best version using a **reinforcement learning–inspired reward function**.

---


## 🧪 How It Works

### Step 1: Add Versions to ChromaDB

```bash
python versioning/chroma_db.py

