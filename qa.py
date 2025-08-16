from transformers import pipeline

def answer_question(question: str, context: str) -> str:
    qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
    answer = qa_pipeline(question=question, context=context)
    return answer['answer']
