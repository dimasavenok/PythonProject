class PrintMixin:
    def __init__(self, price):
        self.__price = price
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.__price}, {self.quantity})"