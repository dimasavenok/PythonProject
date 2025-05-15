class Product:

    def __init__(self, name:str, description:str, price:float, quantity:int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity= quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
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






