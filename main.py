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


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)


if __name__ == "__main__":
    product1 = Product("Laptop", "High-end laptop", 1000, 5)
    product2 = Product("Smartphone", "Latest model", 500, 10)

    category1 = Category("Electronics", "Electronic devices",
                         [product1, product2])
    category2 = Category("Furniture", "Home furniture", [])

    print(f"categories amount: {Category.category_count}")
    print(f"products in categories: {Category.product_count}")
