import chromadb
from chromadb.config import Settings

chroma_client = chromadb.Client(Settings(
    persist_directory=".chroma_db",  # or your choice
    anonymized_telemetry=False
))

def get_or_create_collection(tenant_id: str):
    return chroma_client.get_or_create_collection(name=f"tenant_{tenant_id}")

def embed_and_store_document(collection, text_chunks: list, metadata: dict):
    ids = [f"doc_{i}" for i in range(len(text_chunks))]
    collection.add(
        documents=text_chunks,
        metadatas=[metadata]*len(text_chunks),
        ids=ids
    )

def query_collection(collection, query: str, top_k=3):
    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )
    return results  