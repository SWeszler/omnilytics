from flask import Flask, jsonify
from flask_cors import CORS
import json
import settings
import os
from utils import (
    init_storage,
    generate_sequence,
    save_sequence,
    save_report,
    get_report
)

app = Flask(__name__)
CORS(app)
init_storage()


@app.route('/generate/')
def generate():
    sequence, report = generate_sequence()
    save_sequence(sequence)
    save_report(report)

    return jsonify({'status': 'success', 'data': sequence})


@app.route('/report/')
def report():
    response = {
        'status': 'success',
        'data': get_report()
    }

    return jsonify(response)
