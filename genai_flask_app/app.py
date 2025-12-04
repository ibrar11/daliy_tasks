from flask import Flask, request, jsonify
from model import get_model_response
app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate(): 
    data = request.json
    model_name = data.get('model')
    user_message = data.get('message')

    if not user_message or not model_name:
        return jsonify({"error": "Missing message or model selection"}), 400
    system_prompt = "You are an AI assistant helping with customer inquiries. Provide a concise response."
    try:
        response = get_model_response(model_name, system_prompt, user_message)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    if name == 'main':
        app.run(debug=True)