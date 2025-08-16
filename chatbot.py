from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

def chatbot(prompt: str) -> str:
    generator = pipeline("text-generation", model="gpt2", max_new_tokens=500, temperature=0.7)
    llm = HuggingFacePipeline(pipeline=generator)
    return llm.invoke(prompt)
