import os
import chromadb
from sentence_transformers import SentenceTransformer

class RAGManager:
    def __init__(self, persist_dir="./output/chroma_db"):
        self.client = chromadb.PersistentClient(path=persist_dir)
        self.collection = self.client.get_or_create_collection("invoices")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def add(self, text, metadata):
        emb = self.model.encode([text])[0].tolist()
        self.collection.add(documents=[text], embeddings=[emb], metadatas=[metadata], ids=[metadata["file"]])

    def retrieve(self, query, top_k=3):
        emb = self.model.encode([query])[0].tolist()
        results = self.collection.query(query_embeddings=[emb], n_results=top_k)
        return "\n".join(results.get("documents", [""])[0])
