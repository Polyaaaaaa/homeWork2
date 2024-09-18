import pytest

from main import Category, Product


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
    assert category.category_count == 1
    assert category.product_count == 2
