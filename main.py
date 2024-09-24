

class Product:
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dictionary):
        name = dictionary.get('name')
        description = dictionary.get('description')
        price = dictionary.get('price')
        quantity = dictionary.get('quantity')

        return cls(name, description, price, quantity)


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        self.__products.append(product)

    @property
    def get_products(self):
        products = []
        for product in self.__products:
            products.append(f'{product.name}, {product.price} руб. Остаток: {product.quantity}')

        return products
