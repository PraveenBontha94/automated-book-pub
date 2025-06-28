import chromadb

# Use default settings now (to avoid legacy client error)
client = chromadb.PersistentClient(path="./chroma_store")

# List all collections
collections = client.list_collections()
print("✅ Available collections:")
for c in collections:
    print("-", c.name)

# Get your collection (must match the one created earlier)
collection = client.get_collection("book_versions")

# Define a reward function
def compute_reward(metadata, similarity_score):
    reward = 0.0
    version = metadata.get("version") or metadata.get("source") or ""

    if version == "final":
        reward += 1.5
    elif version == "reviewer":
        reward += 1.0
    elif version == "writer":
        reward += 0.5
    else:  # raw or unknown
        reward += 0.0

    reward += (1 - similarity_score)  # Lower distance = higher similarity
    return reward

# Retrieval with reward-based ranking
def rl_retrieve(query):
    print(f"\n🔍 Query: {query}\n")
    results = collection.query(
        query_texts=[query],
        n_results=4,
        include=["documents", "metadatas", "distances"]
    )

    docs = results["documents"][0]
    metas = results["metadatas"][0]
    dists = results["distances"][0]

    if not docs:
        print("⚠️ No documents found for this query.")
        return

    ranked = []
    for doc, meta, dist in zip(docs, metas, dists):
        reward = compute_reward(meta, dist)
        ranked.append((reward, meta, doc, dist))

    ranked.sort(key=lambda x: x[0], reverse=True)

    best = ranked[0]
    print("🏆 Best Version Based on RL Score:")
    print(f"📘 Version: {best[1].get('version') or best[1].get('source')}")
    print(f"⭐ RL Score: {best[0]:.4f}")
    print(f"📏 Distance: {best[3]:.4f}")
    print(f"\n📝 Snippet:\n{best[2][:500].strip()}...\n")

# Run the search
if __name__ == "__main__":
    rl_retrieve("canoe builder arriving at the beach")
