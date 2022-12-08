import pytest
from app_api.models import Recipe
from app_api import db, app


@pytest.fixture
def testing_client(scope='module'):
    db.create_all()
    recipe = Recipe('Test Recipe', 'Test Ingredients', 'Test Steps', 0, False)
    db.session.add(recipe)
    db.session.commit()

    with app.test_client() as testing_client:
        yield testing_client

    db.drop_all()