import json


import pytest

from src.classed import Category, Product


product1 = Product(
    "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


@pytest.fixture()
def product_samsung():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture()
def category_smart():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )


@pytest.fixture()
def product_iphone():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture()
def category_tv():
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )


# фикстуры для теста utils
@pytest.fixture
def sample_json_file(tmp_path):
    data = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны",
            "products": [
                {
                    "name": "Samsung Galaxy S23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 1200,
                    "quantity": 10,
                },
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 800,
                    "quantity": 20,
                },
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор",
            "products": [
                {
                    "name": "Lg",
                    "description": "Фоновая подсветка",
                    "price": 20,
                    "quantity": 50,
                }
            ],
        },
    ]

    test_file = tmp_path / "test.json"
    with open(test_file, "w", encoding="UTF-8") as f:
        json.dump(data, f)
    return test_file
