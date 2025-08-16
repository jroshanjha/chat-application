from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

def rag(query: str, docs: list) -> str:
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_texts(docs, embeddings)
    retriever = db.as_retriever()

    generator = pipeline("text-generation", model="gpt2", max_new_tokens=1000)
    llm = HuggingFacePipeline(pipeline=generator)

    relevant_docs = retriever.get_relevant_documents(query)
    context = " ".join([d.page_content for d in relevant_docs])

    prompt = f"Answer the question based on context:\n\nContext: {context}\n\nQuestion: {query}\nAnswer:"
    return llm.invoke(prompt)
