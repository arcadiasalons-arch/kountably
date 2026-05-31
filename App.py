from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # This allows your frontend website to securely talk to this server

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "Kountably backend is live, secure, and ready for data."})

if __name__ == '__main__':
    app.run(port=5000)
