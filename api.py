from flask import Flask, jsonify, make_response, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

import json
import random
app = Flask(__name__)

# Prevents the json data to sorted alphabetically
app.config['JSON_SORT_KEYS'] = False

# limit an ip by 100request per hour
limiter = Limiter(app, key_func=get_remote_address,
                  default_limits=["100 per hour"])

with open('greetings/index.json', 'r') as file:
    greetings = json.load(file)


@app.route('/')
def index():
    return "Try: /api/greetings/ , /api/greetings/id/ , /api/greetings/random"


@app.route('/api/greetings/')
def greetings_all():
    return jsonify(greetings)


@app.route('/api/greetings/lang/<language>/')
def greeting_language(language):
    data = []

    for greeting in greetings:
        if greeting['language'] == language.lower():
            data.append(greeting)
    return jsonify(data)


@app.route('/api/greetings/<int:id>/')
def greeting_id(id):
    try:
        greeting = greetings[id]
        return jsonify(greeting)
    except IndexError:
        return jsonify({"Error": {"Code": 404, "Message": "Greeting with the given id was not found."}}), 404


@app.route('/api/greetings/random/')
def greeting_random():
    greeting = random.choice(greetings)
    return jsonify(greeting)


# test
@app.route('/ping')
def pong():
    return "Pong"

# error handler for 429


@app.errorhandler(429)
def ratelimit_handler(e):
    return make_response(jsonify(error=f"rate limit exceeded {e.description}"))

# Whitelist the local ip


@limiter.request_filter
def ip_whitelist():
    return request.remote_addr == '127.0.0.1'


if __name__ == '__main__':
    app.run(debug=True)
