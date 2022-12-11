import requests


category_lookup = requests.get(url="https://opentdb.com/api_category.php").json()['trivia_categories']
categories = {}

parameters = {
    "amount": 10,
    "type": "boolean"
}

for category in category_lookup:
    categories.update({category['id']: category['name']})




print(categories)
api = requests.get(url="https://opentdb.com/api.php?", params=parameters)
api.raise_for_status()
question_data = api.json()['results']
