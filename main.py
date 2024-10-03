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
        name = dictionary.get("name")
        description = dictionary.get("description")
        price = dictionary.get("price")
        quantity = dictionary.get("quantity")

        return cls(name, description, price, quantity)

    # Геттер для цены
    @property
    def price(self):
        return self.__price

    # Сеттер для цены с проверкой
    @price.setter
    def price(self, price):
        if price <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity}"

    def __add__(self, other):
        total_sum = self.__price * self.quantity  + other.__price * other.quantity
        return total_sum


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
    def products(self):
        products = []
        for product in self.__products:
            products.append(
                f"{product.name}, {product.price} руб. Остаток: {product.quantity}"
            )

        return products

    def __str__(self):
        return f"{self.name}, количество продуктов: {Category.product_count} шт "


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
