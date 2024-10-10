from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def new_product(self):
        pass

    @abstractmethod
    def price(self):
        pass


class Product(BaseProduct):
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
        if type(self) is type(other):
            total_sum = self.__price * self.quantity + other.__price * other.quantity
            return total_sum
        else:
            return TypeError


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
        if not isinstance(product, Product):
            print(
                """вызывана ошибка ValueError, т.к. Складывать можно только смартфонов,
                траву газонную или другие продукты."""
            )
            raise ValueError(
                "Складывать можно только смартфонов, траву газонную или другие продукты."
            )
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


class Smartphone(Product):
    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
