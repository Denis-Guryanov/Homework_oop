import json

import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_1():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture
def product_2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product_3():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def product_4():
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def product_samsung():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture
def product_iphone():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def category_tv(product_4):
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product_4],
    )


@pytest.fixture
def category_smart(product_1, product_2, product_3):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product_1, product_2, product_3],
    )


@pytest.fixture
def sample_json_file(tmp_path):
    data = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy S23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 1200,
                    "quantity": 10,
                },
                {
                    "name": "iPhone 14",
                    "description": "512GB, Gray space",
                    "price": 1100,
                    "quantity": 5,
                },
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
            "products": [],
        },
    ]
    file_path = tmp_path / "sample.json"
    file_path.write_text(json.dumps(data))
    return file_path


@pytest.fixture
def product_str_1(product_1):
    return f"{product_1.name}, {product_1.price} руб. Остаток: {product_1.quantity} шт."


@pytest.fixture
def product_str_2(product_2):
    return f"{product_2.name}, {product_2.price} руб. Остаток: {product_2.quantity} шт."


@pytest.fixture
def counter(product_1, product_2):
    return product_1.price * product_1.quantity + product_2.price * product_2.quantity


@pytest.fixture
def counter_2(product_2, product_3):
    return product_2.price * product_2.quantity + product_3.price * product_3.quantity


@pytest.fixture
def sum_counter(category_smart):
    return f"{category_smart.name}, {category_smart.products[0].quantity + category_smart.products[1].quantity + category_smart.products[2].quantity} шт."
