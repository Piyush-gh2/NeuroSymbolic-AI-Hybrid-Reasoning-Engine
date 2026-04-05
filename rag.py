from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def load_knowledge():
    with open("knowledge.txt", "r") as f:
        docs = f.readlines()
    return docs

def build_index(docs):
    embeddings = model.encode(docs)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return index, embeddings

def retrieve(query, docs, index):
    q_emb = model.encode([query])
    D, I = index.search(np.array(q_emb), k=2)
    return [docs[i] for i in I[0]]