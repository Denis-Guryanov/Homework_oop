from src.category import Category
from src.product import Product
from src.utils import create_object_from_json, read_json



def test_read_json(sample_json_file):
    result = read_json(sample_json_file)
    assert isinstance(result, list)  # Проверяем, что возвращаемое значение - список
    assert len(result) == 2  # Убедимся, что в JSON две категории
    assert result[0]["name"] == "Смартфоны"  # Проверяем имя первой категории


# Тест для функции create_object_from_json
def test_create_object_from_json(sample_json_file):
    data = read_json(sample_json_file)
    categories = create_object_from_json(data)

    assert len(categories) == 2  # Проверяем, что созданы два объекта Category
    assert isinstance(
        categories[0], Category
    )  # Убедимся, что элементы списка являются объектами Category

    # Проверяем продукты внутри первой категории
    electronics = categories[0]
    assert electronics.name == "Смартфоны"
    assert len(electronics.products) == 2
    assert isinstance(electronics.products[0], Product)
    assert electronics.products[0].name == "Samsung Galaxy S23 Ultra"
    assert electronics.products[0].price == 1200
    assert electronics.products[0].quantity == 10
