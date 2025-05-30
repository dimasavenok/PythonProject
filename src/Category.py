from itertools import product

from src.Product import Product
from src.errors.ZeroQuantityError import ZeroQuatityError


class Category:
    category_count = 0
    product_count = 0


    def __init__(self, name:str, description:str, product:list[Product]):
        self.name = name
        self.description = description
        self.__product = product
        Category.category_count += 1
        Category.product_count += len(product)

    def __str__(self):
        summ = 0
        for product in self.__product:
            summ += product.quantity
        return f"{self.name}, количество продуктов: {summ} шт."


    @property
    def product(self):
        result = []
        for i in self.__product:
            result.append(f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт.")
        return "\n".join(result)

    def add_product(self, product):
        """ Добавляет продукт в категорию и увеличивает счётчик """
        if isinstance(product, Product) or issubclass(product, Product):
            try:
                self.__product.append(product)
                self.product_count += 1
            except ZeroQuatityError:
                print("Колличество равно нулю")
            finally:
                print("обработка добавления товара завершена.")
        else:
            raise TypeError


    def middle_price(self):
        try:
            return sum(product.price * product.quantity for product in self.__product) / sum(product.quantity for product in self.__product)
        except ZeroDivisionError:
            return 0






