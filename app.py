from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from querying import generate_response  # Importing from your querying.py

app = Flask(__name__)
api = Api(app)

# Define a resource for the chatbot
class ChatBotAPI(Resource):
    def post(self):
        # Parse the user input from the JSON request
        data = request.get_json()
        user_question = data.get('question')

        if not user_question:
            return jsonify({"error": "No question provided"}), 400
        
        # Generate chatbot response using querying.py logic
        try:
            response = generate_response(user_question)
            return jsonify({"response": response})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

# Add the chatbot resource to the API
api.add_resource(ChatBotAPI, "/chat")

if __name__ == "__main__":
    # Start the Flask app
    app.run(debug=True)
