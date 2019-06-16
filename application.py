import recipe_finder
import recipe_utils
import time
from lxml import html
from flask import Flask
from flask_cors import CORS
from flask import request
from flask import jsonify
from flask import Response
import requests
import os
from os.path import join, dirname
import asyncio

application = Flask(__name__)
cors = CORS(application, resources={r"*": {"origins": "*"}})


@application.route('/', methods=['GET'])
def hello_world():
    return('Hello World!')


@application.route('/get_recipes', methods=['GET'])
def get_recipes():
    pantry_items = ["bread", "milk", "egg", "soda", "coffee", "water", "paprika", "red pepper", "chili pepper",
                    "green onion", "tomato", "onion", "salami", "ham", "turkey", "salt", "pepper", "garlic powder",
                    "onion powder", "thyme", "broccoli", "banana", "strawberry", "strawberries", "blackberry",
                    "blackberries", "blueberry", "blueberries", "lettuce", "bacon", "sausage", "hamburger",
                    "peas", "corn", "cottage cheese", "cheddar cheese", "mozzarella cheese", "cream cheese", "chicken wing",
                    "chicken breast", "cayenne pepper", "potato"]

    recipes = recipe_finder.search_for_recipes(pantry_items)
    results = recipe_utils.recipes_to_json(recipes)

    return results


if __name__ == '__main__':
    application.run()
