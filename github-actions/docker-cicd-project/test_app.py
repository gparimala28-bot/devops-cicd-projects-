"""Test Flask application."""

from app import app


def test_home():
    """Test home route."""
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200