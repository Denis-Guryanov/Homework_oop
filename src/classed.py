class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.category_count = None
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count = len(products) if products else 0