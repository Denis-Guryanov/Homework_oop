class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count = len(products) if products else 0

    @property
    def products(self):
        return self.__products

    def add_product(self, new_products):
        self.__products.append(new_products)
        Category.product_count += 1

    @property
    def product_list(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток {product.quantity} шт.\n "
        return product_str

    def __str__(self):
        counter = sum(product.quantity for product in self.__products)
        return f"{self.name}, {counter} шт.\n"
