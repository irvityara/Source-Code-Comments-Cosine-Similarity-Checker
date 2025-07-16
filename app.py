import os
from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# If you were using the Hugging Face API with token
hf_token = os.getenv("HF_API_TOKEN")

model = SentenceTransformer('all-MiniLM-L6-v2')

@app.route('/')
def home():
    return "API is working!"

@app.route('/similarity', methods=['POST'])
def similarity():
    data = request.json
    text1 = data.get('text1', '')
    text2 = data.get('text2', '')

    if not text1 or not text2:
        return jsonify({'error': 'Both texts are required'}), 400

    embeddings = model.encode([text1, text2])
    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]

    return jsonify({'similarity': round(score, 4)})

if __name__ == '__main__':
    app.run(debug=True)
