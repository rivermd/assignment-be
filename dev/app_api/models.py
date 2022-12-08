from app_api import db
from datetime import datetime
import string, random

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    ingredients = db.Column(db.String(32), nullable=False)
    steps = db.Column(db.String(32), nullable=False)
    rating = db.Column(db.Integer, nullable=False, default=0)
    favorite = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return '<Event %r>' % self.name

    def __init__(self, name, ingredients, steps, rating, favorite):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        self.rating = rating
        self.favorite = favorite