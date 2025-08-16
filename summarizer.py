from transformers import pipeline

def summarize(text: str) -> str:
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=600, min_length=100, do_sample=False)
    return summary[0]['summary_text']
