from typing import Union

from src.BaseProduct import BaseProduct
from src.PrintMixin import PrintMixin
from src.errors.ZeroQuantityError import ZeroQuatityError


class Product(BaseProduct, PrintMixin):

    def __init__(self, name:str, description:str, price:float, quantity:int):
        if quantity == 0:
            raise ZeroQuatityError("Товар с нулевым количеством не может быть добавлен.")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity= quantity
        super().__init__(price)

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."


    def __add__(self, other: Union["Product", int, float]):
        if type(self) != type(other):
            raise TypeError
        other_sum = other.price * other.quantity
        return other_sum + self.__price * self.quantity


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0 and self.__price > new_price:
            choice = input("Вы уверены что хотите понизить цену? (y/n): ")
            if choice == "y":
                self.__price = new_price
        elif new_price > 0:
            self.__price = new_price
        elif new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, dict_of_product):
        name = dict_of_product['name']
        description = dict_of_product['description']
        price = dict_of_product['price']
        quantity = dict_of_product['quantity']

        new_product = Product(name, description, price, quantity)
        return new_product






