import json
import os

from src.classed import Category, Product


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_object_from_json(data):
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories


# if __name__ == '__main__':
#     products= read_json('../date/products.json')
#     cat = create_object_from_json(products)
#
#     print(cat[1].name)
#     print(cat[1].description)
#     print(cat[1].products)
