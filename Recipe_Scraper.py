import requests
from bs4 import BeautifulSoup
from csv import writer
import time
import random


def obtain_recipes(urls):

    print("Traversing urls for recipe information...")
    with open('recipes.csv', 'a', newline='') as csv_file:
        csv_writer = writer(csv_file)

        count = 0
        for url in urls:
            if "foodnetwork.com" in url:
                try:
                    # Obtain Web page
                    response = requests.get(url)
                    soup = BeautifulSoup(response.text, 'html.parser')

                    count += 1
                    # Obtain recipe name
                    recipe_title = soup.find(
                        class_='o-AssetTitle__a-HeadlineText').get_text().replace('\n', '')

                    print(str(count) + ". Gathering information for " +
                          str(recipe_title))

                    # Save recipe URL
                    recipe_url = url

                    # Obtain ingredients div from webpage
                    list_of_ingredients = soup.find_all(
                        class_='o-Ingredients__a-Ingredient')

                    # Gather ingredients list from recipe
                    ingredients = []
                    for ingredient_item in list_of_ingredients:
                        ingredients.append(ingredient_item.get_text())

                    # Write recipe to CSV
                    csv_writer.writerow(
                        [recipe_title, recipe_url, ingredients])

                    # Time out to prevent banning
                    #time.sleep(random.randint(1, 3))
                except:
                    print("Could not complete for this recipe.")


def obtain_urls(entry_url):
    print("Gathering recipe urls...")

    # Get web page
    response = requests.get(
        entry_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find recipe urls
    recipe_urls = soup.find_all(class_='m-PromoList__a-ListItem')

    # Define urls list
    urls = []

    # Obtain recipe urls from web page
    for recipe_url in recipe_urls:
        url = recipe_url.find('a')['href']

        if "http:" not in url:
            url = "http:" + url

        urls.append(url)

    print("Done.")
    return urls


def handle_pagination(num_of_pages):
    for page in range(1, num_of_pages + 1):
        url = "https://www.foodnetwork.com/recipes/recipes-a-z/xyz/p/" + \
            str(page)

        urls_list = obtain_urls(url)

        obtain_recipes(urls_list)


if __name__ == "__main__":

    # Track elapsed time to gather recipes
    start_time = time.time()
    handle_pagination(4)
    print("Elapsed time: " + str(time.time() - start_time))
