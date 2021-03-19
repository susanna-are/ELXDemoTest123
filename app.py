from flask import Flask
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello World from Flask using CORS."

if __name__ == '__main__':
    app.run()