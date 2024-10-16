import pytest

from main import Category, LawnGrass, Product, Smartphone


@pytest.fixture
def product():
    return Product("Laptop", "High-end laptop", 1000, 5)


def test_product_init(product):
    assert product.name == "Laptop"
    assert product.description == "High-end laptop"
    assert product.price == 1000
    assert product.quantity == 5


@pytest.fixture
def category():
    product1 = Product("Laptop", "High-end laptop", 1000, 5)
    product2 = Product("Smartphone", "Latest model", 500, 10)
    return Category("Electronics", "Electronic device", [product1, product2])


def test_category_init(category):
    assert category.name == "Electronics"
    assert category.description == "Electronic device"
    assert len(category.products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_get_products():
    # Создаем экземпляр класса Category
    products = [
        Product("Product1", "Description1", 100, 5),
        Product("Product2", "Description2", 200, 10),
    ]
    category = Category("Category1", "Description1", products)

    # Получаем список продуктов
    products_list = category.products

    # Проверяем, что список продуктов содержит ожидаемые элементы
    assert len(products_list) == 2
    assert products_list[0] == "Product1, 100 руб. Остаток: 5"
    assert products_list[1] == "Product2, 200 руб. Остаток: 10"


def test_add_product():
    # Создаем экземпляр класса Category
    products = [Product("Product1", "Description1", 100, 5)]
    category = Category("Category1", "Description1", products)

    # Добавляем новый продукт
    new_product = Product("Product2", "Description2", 200, 10)
    category.add_product(new_product)

    # Получаем список продуктов
    products_list = category.products

    # Проверяем, что продукт добавлен в список
    assert len(products_list) == 2
    assert products_list[1] == "Product2, 200 руб. Остаток: 10"

    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    smartphone2 = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000, 8, 98.2, "15", 512, "Gray space"
    )
    smartphone3 = Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий",
    )

    # Создаем категорию для смартфонов
    category_smartphones = Category(
        "Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2]
    )

    # Добавляем новый смартфон в категорию
    category_smartphones.add_product(smartphone3)

    # Получаем список продуктов в категории смартфонов
    smartphones_list = category_smartphones.products

    # Проверяем, что смартфон добавлен в список
    assert len(smartphones_list) == 3
    assert smartphones_list[2] == "Xiaomi Redmi Note 11, 31000 руб. Остаток: 14"

    assert Category.product_count == 9


def test_set_price():
    # Создаем экземпляр класса Product
    product = Product("Product1", "Description1", 100, 5)

    # Устанавливаем новую цену
    product.price = 150
    assert product.price == 150

    # Проверяем, что нельзя установить нулевую или отрицательную цену
    with pytest.raises(
        ValueError, match="Цена не должна быть нулевая или отрицательная"
    ):
        product.price = 0
    assert product.price == 150

    with pytest.raises(
        ValueError, match="Цена не должна быть нулевая или отрицательная"
    ):
        product.price = -100
    assert product.price == 150


def test_get_price():
    # Создаем экземпляр класса Product
    product = Product("Product1", "Description1", 100, 5)

    # Проверяем, что get_price возвращает правильную цену
    assert product.price == 100


def test_new_product():
    # Создаем словарь с данными продукта
    product_data = {
        "name": "Product1",
        "description": "Description1",
        "price": 100,
        "quantity": 5,
    }

    # Создаем новый продукт с использованием new_product
    product = Product.new_product(product_data)

    # Проверяем, что продукт создан правильно
    assert product.name == "Product1"
    assert product.description == "Description1"
    assert product.price == 100
    assert product.quantity == 5


def test__str__product():
    product = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000, 5
    )
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5"


def test__str__category():
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000, 14)
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    assert str(category) == "Смартфоны, количество продуктов: 12 шт "


def test__add__product():
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000, 8)
    assert product1 + product2 == 2580000

    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    smartphone2 = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000, 8, 98.2, "15", 512, "Gray space"
    )
    smartphone3 = Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий",
    )
    assert smartphone1 + smartphone2 == 2580000
    assert smartphone2 + smartphone3 == 2114000

    grass1 = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    grass2 = LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )
    assert grass1 + grass2

    assert smartphone1 + grass1 == TypeError


def test_initialisation_mixin(capsys):
    Product("Product1", "Description1", 100, 5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product('Product1', 'Description1', 100, 5)"


# def test_middle_price():
#     with pytest.raises(ValueError):
#         Category("fhjf", "jkkdd", [])


def test_product_init():
    # product = Product("bdjd", "jdfhjd", 123, 0)
    with pytest.raises(ValueError):
        Product("fhjf", "jkkdd", 123, 0)