from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def new_product(self):
        pass

    @abstractmethod
    def price(self):
        pass


class InitialisationMixin:
    def __init__(self):
        # self.quantity = self.quantity
        # self.price = self.price
        # self.description = self.description
        # self.name = self.name
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"


class Product(InitialisationMixin, BaseProduct):
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        else:
            self.quantity = quantity
        super().__init__()

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

    def middle_price(self):
        try:
            summ = 0
            for product in self.__products:
                summ += product.price

            avg_price = summ / len(self.__products)
        except ZeroDivisionError:
            print("на ноль делить нельзя")
        except TypeError:

            print("Ошибка типа")
        else:
            return avg_price
        finally:
            print("функция middle_price завершила работу")


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


# if __name__ == '__main__':
#     try:
#         product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
#     except ValueError as e:
#         print(
#             "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")
#     else:
#         print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")
#
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])
#
#     print(category1.middle_price())
#
#     category_empty = Category("Пустая категория", "Категория без продуктов", [])
#     print(category_empty.middle_price())
