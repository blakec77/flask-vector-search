from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'sk-EE2UucEwgWnrEtCluau-LDgh7kVmhq49z1aRQii2umT3BlbkFJd3vr9SVEkkkbDngFzepCsMWlf7pgD6BRTArIQM0DEA'

@app.route('/vector_search', methods=['POST'])
def vector_search():
    data = request.json
    query = data['query']

    # Generate embedding
    embedding = generate_embedding(query)

    # Search vector store
    results = search_vector_store(embedding)

    return jsonify(results)

def generate_embedding(query):
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=[query]
    )
    return response['data'][0]['embedding']

def search_vector_store(embedding):
    search_response = openai.VectorStore.search(
        vector_store_id="vs_Srkl2boUdnlLGXd7XD4kthJL",  # Replace with your vector store ID
        query_embedding=embedding,
        top_k=5
    )
    return [result['metadata']['text'] for result in search_response['results']]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, world! Your Flask app is running."

if __name__ == '__main__':
    app.run()
