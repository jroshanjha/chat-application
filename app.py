from chatbot import chatbot
from rag import rag
from summarizer import summarize
from qa import answer_question

if __name__ == "__main__":
    print("Choose Mode:")
    print("1. Chatbot")
    print("2. RAG")
    print("3. Summarization")
    print("4. Question Answering")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        user_input = input("You: ")
        print("🤖 Chatbot:", chatbot(user_input))

    elif choice == "2":
        docs = [
            "Machine learning is a subset of AI.",
            "LangChain helps build LLM-powered apps.",
            "Transformers library powers many NLP tasks."
        ]
        query = input("Enter your question: ")
        print("📚 RAG Answer:", rag(query, docs))

    elif choice == "3":
        text = input("Enter text to summarize: ")
        print("📝 Summary:", summarize(text))

    elif choice == "4":
        context = input("Enter context: ")
        question = input("Enter question: ")
        print("🔍 QA Answer:", answer_question(question, context))

    else:
        print("Invalid choice!")

# if __name__ == "__main__":
#     print("Welcome to the NLP Toolkit!")
#     print("This toolkit allows you to perform various NLP tasks using Hugging Face models.")
#     print("You can choose from Chatbot, RAG, Summarization, or Question Answering.")
#     print("Let's get started!")
#     app.run(debug=True) 

# from flask import Flask, request, jsonify           
# app = Flask(__name__)
# @app.route('/')
# def home():
#     return "Welcome to the NLP Toolkit! Use the endpoints for Chatbot, RAG, Summarization, or Question Answering."
# @app.route('/chatbot', methods=['POST'])
# def chatbot_endpoint():
#     data = request.json
#     prompt = data.get('prompt', '')
#     response = chatbot(prompt)
#     return jsonify({'response': response})
# @app.route('/rag', methods=['POST'])
# def rag_endpoint():
#     data = request.json
#     query = data.get('query', '')
#     docs = data.get('docs', [])
#     response = rag(query, docs)
#     return jsonify({'response': response})
# @app.route('/summarize', methods=['POST'])
# def summarize_endpoint():
#     data = request.json
#     text = data.get('text', '')
#     response = summarize(text)
#     return jsonify({'summary': response})
# @app.route('/qa', methods=['POST'])
# def qa_endpoint():
#     data = request.json
#     question = data.get('question', '')
#     context = data.get('context', '')
#     response = answer_question(question, context)
#     return jsonify({'answer': response})
