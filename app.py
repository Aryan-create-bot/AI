from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Use your OpenAI API key (better to set as ENV variable)
openai.api_key = os.getenv("OPENAI_API_KEY") or "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"

@app.route('/api/v1', methods=['GET'])
def ai_reply():
    question = request.args.get('question', '')
    if not question:
        return jsonify({'error': 'No question provided'}), 400

    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Answer clearly: {question}",
            max_tokens=200,
            temperature=0.7
        )
        answer = response.choices[0].text.strip()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'reply': answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)