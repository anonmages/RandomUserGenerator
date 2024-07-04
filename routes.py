from flask import Flask, render_template, jsonify, request
import os
import requests
from flask_caching import Cache

app = Flask(__name__)

app.config['CACHE_TYPE'] = 'simple'
cache = Cache(app)

random_user_url = os.getenv('RANDOM_USER_API_URL', 'https://randomuser.me/api/')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate', methods=['GET'])
def generate_random_user():
    return generate_user_with_nationality()

@app.route('/generate/<nationality>', methods=['GET'])
@cache.cached(timeout=300, query_string=True)
def generate_user_with_nationality(nationality=None):
    params = {}
    if nationality:
        params['nat'] = nationality
    cache_key = 'nationality_{}'.format(nationality if nationality else 'all')
    cached_result = cache.get(cache_key)
    if cached_result:
        return cached_result

    response = requests.get(random_user_url, params=params)
    if response.ok:
        result = jsonify(response.json())
        cache.set(cache_key, result, timeout=300)
        return result
    else:
        return jsonify({"error": "Failed to fetch user data"}), 500

if __name__ == "__main__":
    app.run(debug=True)