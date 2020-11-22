from flask import Flask, jsonify
import random
import string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def generate():
    sequence = ''
    for i in range(20):
        sequence += random.choice(string.ascii_uppercase + string.digits)

    return jsonify({'sequence': sequence})
