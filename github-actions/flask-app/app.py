from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! I have successfully automated a CI/CD pipeline using GitHub Actions and deployed this Flask application on a self-hosted runner."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
