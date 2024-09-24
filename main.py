class Product:
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dictionary):
        name = dictionary.get('name')
        description = dictionary.get('description')
        price = dictionary.get('price')
        quantity = dictionary.get('quantity')

        return cls(name, description, price, quantity)

    # Геттер для цены
    @property
    def get_price(self):
        return self.__price

    # Сеттер для цены с проверкой
    @get_price.setter
    def get_price(self, price):
        if price <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price


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
        Category.product_count += 1

    @property
    def get_products(self):
        products = []
        for product in self.__products:
            products.append(f'{product.name}, {product.get_price} руб. Остаток: {product.quantity}')

        return products


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(category1.get_products)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000, 7)
    category1.add_product(product4)
    print(category1.get_products)
    print(Category.product_count)

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000,
         "quantity": 5})
    print(new_product.name)
    print(new_product.description)
    print(new_product.get_price)
    print(new_product.quantity)

    new_product.set_price = 800
    print(new_product.get_price)

    result = new_product.set_price = -100
    if result:
        print(result)
    print(new_product.get_price)

    result = new_product.set_price = 0
    if result:
        print(result)
    print(new_product.get_price)