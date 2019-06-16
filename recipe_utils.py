import json


def recipes_to_json(recipes):
    recipes_json = json.dumps(recipes)
    print(recipes_json)
