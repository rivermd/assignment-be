from flask import Flask, request
from app_api import db, app
from app_api.models import Recipe


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/skull', methods=['GET'])
def skull():
    return 'Hi! This is the BACKEND SKULL! 💀'

@app.routes('/recipes', methods=['POST'])
def create_recipe():
    name = request.json['name']
    rating = request.json['rating']
    ingredients = request.json['ingredients']
    steps = request.json['steps']
    favorite = request.json['favorite']
    recipe = Recipe(name, rating, ingredients, steps, favorite)
    db.session.add(recipe)
    db.session.commit()
    return format_recipe(recipe)

@app.routes('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    return {'recipes': [format_recipe(recipe) for recipe in recipes]}

@app.routes('/recipes/<int:id>', methods=['GET'])
def get_recipe(id):
    recipe = Recipe.query.get(id)
    return format_recipe(recipe)

@app.routes('/recipes/<int:id>', methods=['PUT'])
def update_recipe(id):
    recipe = Recipe.query.get(id)
    recipe.name = request.json['name']
    recipe.rating = request.json['rating']
    recipe.favorite = request.json['favorite']
    db.session.commit()
    return format_recipe(recipe)

@app.routes('/recipes/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = Recipe.query.get(id)
    db.session.delete(recipe)
    db.session.commit()
    return format_recipe(recipe)

def format_recipe(recipe):
    return {
        'id': recipe.id,
        'name': recipe.name,
        'rating': recipe.rating,
        'ingredients': recipe.ingredients,
        'steps': recipe.steps,
        'favorite': recipe.favorite,
        'created_at': recipe.created_at
    }

#@app.route('/accounts', methods=['POST'])
#def create_account():
#    name = request.json['name']
#    currency = request.json['currency']
#    account = Account(name, currency)
#    db.session.add(account)
#    db.session.commit()
#    return format_account(account)

#@app.route('/accounts', methods=['GET'])
#def get_accounts():
#    accounts = Account.query.all()
#    return {'accounts': [format_account(account) for account in accounts]}

#@app.route('/accounts/<int:id>', methods=['GET'])
#def get_account(id):
#    account = Account.query.get(id)
#    return format_account(account)

#@app.route('/accounts/<int:id>', methods=['PUT'])
#def update_account(id):
#    account = Account.query.get(id)
#    account.name = request.json['name']
#    db.session.commit()
#    return format_account(account)

#@app.route('/accounts/<int:id>', methods=['DELETE'])
#def delete_account(id):
#    account = Account.query.get(id)
#    db.session.delete(account)
#    db.session.commit()
#    return format_account(account)

#def format_account(account):
#    return {
#        'id': account.id,
#        'name': account.name,
#        'account_number': account.account_number,
#        'balance': account.balance,
#        'currency': account.currency,
#        'status': account.status,
#        'created_at': account.created_at
#    }