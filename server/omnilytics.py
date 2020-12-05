from flask import Flask, jsonify, send_file
from flask_cors import CORS
import os
from utils import (
    generate_sequence,
    save_sequence,
    save_report,
    get_report,
    get_output
)

app = Flask(__name__)
CORS(app)


@app.route('/generate/<timestamp>')
def generate(timestamp):
    sequence, report = generate_sequence()
    save_sequence(sequence, timestamp=timestamp)
    save_report(report, timestamp=timestamp)

    return jsonify({'status': 'success', 'data': sequence})


@app.route('/report/<timestamp>')
def report(timestamp):
    response = {
        'status': 'success',
        'data': get_report(timestamp)
    }

    return jsonify(response)


@app.route('/download/<timestamp>')
def download(timestamp):
    return send_file(get_output(timestamp), as_attachment=True)
