import pytest
from main import Category, Product

@pytest.fixture
def product():
    return Product("Laptop", "High-end laptop", 1000, 5)

def test_product_init(product):
    assert product.name == "Laptop"
    assert product.description == "High-end laptop"
    assert product.get_price == 1000
    assert product.quantity == 5

@pytest.fixture
def category():
    product1 = Product("Laptop", "High-end laptop", 1000, 5)
    product2 = Product("Smartphone", "Latest model", 500, 10)
    return Category("Electronics", "Electronic device", [product1, product2])

def test_category_init(category):
    assert category.name == "Electronics"
    assert category.description == "Electronic device"
    assert len(category.get_products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2

def test_get_products():
    # Создаем экземпляр класса Category
    products = [Product("Product1", "Description1", 100, 5), Product("Product2", "Description2", 200, 10)]
    category = Category("Category1", "Description1", products)

    # Получаем список продуктов
    products_list = category.get_products

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
    products_list = category.get_products

    # Проверяем, что продукт добавлен в список
    assert len(products_list) == 2
    assert products_list[1] == "Product2, 200 руб. Остаток: 10"

def test_set_price():
    # Создаем экземпляр класса Product
    product = Product("Product1", "Description1", 100, 5)

    # Устанавливаем новую цену
    product.get_price = 150
    assert product.get_price == 150

    # Проверяем, что нельзя установить нулевую или отрицательную цену
    with pytest.raises(ValueError, match="Цена не должна быть нулевая или отрицательная"):
        product.get_price = 0
    assert product.get_price == 150

    with pytest.raises(ValueError, match="Цена не должна быть нулевая или отрицательная"):
        product.get_price = -100
    assert product.get_price == 150

def test_get_price():
    # Создаем экземпляр класса Product
    product = Product("Product1", "Description1", 100, 5)

    # Проверяем, что get_price возвращает правильную цену
    assert product.get_price == 100

def test_new_product():
    # Создаем словарь с данными продукта
    product_data = {
        "name": "Product1",
        "description": "Description1",
        "price": 100,
        "quantity": 5
    }

    # Создаем новый продукт с использованием new_product
    product = Product.new_product(product_data)

    # Проверяем, что продукт создан правильно
    assert product.name == "Product1"
    assert product.description == "Description1"
    assert product.get_price == 100
    assert product.quantity == 5
