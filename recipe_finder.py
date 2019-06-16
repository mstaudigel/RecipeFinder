import csv
from bs4 import BeautifulSoup
import requests


def search_for_recipes(pantry_items):

    recipe_count = 0

    recipes = {}

    with open('recipes.csv') as inputFile:
        for row in csv.reader(inputFile):
            total_amount_of_usable_pantry_items = 0

            recipe_ingredients = row[2]
            recipe_ingredients = recipe_ingredients.replace("[", "")
            recipe_ingredients = recipe_ingredients.replace("]", "")
            recipe_ingredients = recipe_ingredients.split("', ")

            # For each ingredient in recipe

            for pantry_item in pantry_items:
                for ingredient in recipe_ingredients:
                    if pantry_item in ingredient:
                        total_amount_of_usable_pantry_items += 1
                        break

            if ((total_amount_of_usable_pantry_items / len(recipe_ingredients))*100 > 95):
                recipe_count += 1
                recipes[row[0]] = row[1]

        return recipes


def get_recipe_images(recipes):
    list_of_images = []

    for recipe in recipes:
        try:
            response = requests.get(recipe)
            soup = BeautifulSoup(response.text, 'html.parser')

            recipe_media = soup.find(
                class_="o-RecipeLead__m-RecipeMedia")

            recipe_img = "https:" + str(recipe_media.find(
                'img')["src"])
        except:
            recipe_img = "Image not found"

        list_of_images.append(recipe_img)

    return list_of_images
