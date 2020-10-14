from flask import Flask, jsonify, make_response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

import json
import random
app = Flask(__name__)
# Prevents the json data to sort alphabetically
app.config['JSON_SORT_KEYS'] = False

limiter = Limiter(app, key_func=get_remote_address,
                  default_limits=["100 per hour"])

with open('greetings/index.json', 'r') as file:
    greetings = json.load(file)


@app.route('/')
def index():
    return "Hello World"


@app.route('/api/greetings/')
def greetings_all():
    return jsonify(greetings)


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


@app.route('/ping')
def pong():
    return "Pong"


@app.errorhandler(429)
def ratelimit_handler(e):
    return make_response(jsonify(error=f"rate limit exceeded {e.description}"))


if __name__ == '__main__':
    app.run(debug=True)
