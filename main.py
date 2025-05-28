from src.Product import Product
from src.Category import Category


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)



    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})


    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)


    print(category1.name)
    print(category1.description)
    print(len(category1.product))
    print(category1.category_count)
    print(category1.product_count)
    print(category2.product)
    new_product2 = Product.new_product(
        {"name": "Samsung2 Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 2,
         "quantity":2})
    category2.add_product(new_product2)
    print(category2.product)