from app_api.models import Recipe
import pytest

def test_create_recipe():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, status and created_at fields are defined correctly
    """
    recipe = Recipe('Chocolate Cookies', 'Chocolate, Flour, Sugar, Butter', 'Mix all ingredients', 0, False)
    assert recipe.name == 'Chocolate Cookies'
    assert recipe.ingredients == 'Chocolate, Flour, Sugar, Butter'
    assert recipe.steps == 'Mix all ingredients'
    assert recipe.rating == 0
    assert recipe.favorite == False