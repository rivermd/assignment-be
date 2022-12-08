#from app_api import app
from flask import Flask
import pytest
from conftest import testing_client


app = Flask(__name__)

def test_get_recipe(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/recipe' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/recipes')
    assert response.status_code == 200

def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404

def test_create_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/recipe' page is posted to (POST)
    THEN check the response is valid
    """
    response = testing_client.post('/recipes', json={'name': 'Chocolate Cookies', 'ingredients': 'Chocolate, Flour, Sugar, Butter', 'steps': 'Mix all ingredients', 'rating': 0, 'favorite': False})
    assert response.status_code == 200