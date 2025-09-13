from flask import Flask, request, jsonify
from transformers import pipeline
app = Flask(__name__)
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
@app.route('/api/v1', methods=['GET'])
def ai_qa_get():
    question = request.args.get('question', '')
    context = request.args.get('context', '')
    if not question:
        return jsonify({'error': 'No question provided'}), 400
    if not context:
        context = (
            "Nepal is a country in South Asia. "
            "Sita is a Sanskrit name. "
            "Nepal has a rich history of kings and culture. "
            "Mount Everest is the highest mountain in the world. "
            "... add more knowledge here ..."
        )
    result = qa_pipeline(question=question, context=context)
    return jsonify({'reply': result['answer']})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)