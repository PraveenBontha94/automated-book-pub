import chromadb
from datetime import datetime

client = chromadb.PersistentClient(path="./chroma_store")  # ✅ Correct new format
collection = client.get_or_create_collection("book_versions")


def add_version(version_name, content, metadata=None):
    metadata = metadata or {}
    doc_id = f"{version_name}_{datetime.now().timestamp()}"
    
    collection.add(
        documents=[content],
        metadatas=[{"version": version_name, **metadata}],
        ids=[doc_id]
    )
    print(f"✅ Added '{version_name}' to ChromaDB.")

def search_versions(query_text, n_results=3):
    results = collection.query(
        query_texts=[query_text],
        n_results=n_results
    )
    return results

if __name__ == "__main__":
    # ✅ Add different versions to ChromaDB
    add_version("raw", open("outputs/raw_chapter.txt", encoding="utf-8").read(), metadata={"version": "raw", "source": "scraper"})
    add_version("writer", open("outputs/version_1_ai_writer.txt", encoding="utf-8").read(), metadata={"version": "writer", "author": "llama3"})
    add_version("reviewer", open("outputs/version_2_ai_reviewer.txt", encoding="utf-8").read(), metadata={"version": "reviewer", "author": "llama3"})
    add_version("final", open("outputs/version_3_final.txt", encoding="utf-8").read(), metadata={"version": "final", "editor": "human"})

    # 🔍 Semantic search
    query = "canoe builder"
    results = search_versions(query)

    print(f"\n🔍 Semantic Search Query: '{query}'\nTop Matches:\n")

    for i, doc in enumerate(results["documents"][0]):
        meta = results["metadatas"][0][i]
        dist = results["distances"][0][i]
        print(f"--- Result {i+1} ---")
        print(f"📘 Version: {meta.get('version')}")
        print(f"📏 Distance: {dist:.4f}")
        print(f"📝 Snippet: {doc[:300].strip()}...\n")

