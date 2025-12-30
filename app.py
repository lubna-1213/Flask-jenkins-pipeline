from flask import Flask
from app import app  # Ensure app.py is in root

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Jenkins CI/CD on Windows!"

if __name__ == "__main__":
    app.run()
