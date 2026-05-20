"""Simple Flask application for Docker CI/CD demo."""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    """Return success message."""
    return (
        "Built and deployed a complete CI/CD pipeline"
        "using GitHub Actions, Docker, Docker Hub, and AWS EC2 for automated application deployment."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)