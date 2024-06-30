from flask import Flask, render_template, jsonify
import os
import requests

app = Flask(__name__)

random_user_url = os.getenv('RANDOM_USER_API_URL', 'https://randomuser.me/api/')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate', methods=['GET'])
def generate_random_user():
    response = requests.get(random_user_url)
    if response.ok:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch user data"}), 500

if __name__ == "__main__":
    app.run(debug=True)