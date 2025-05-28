from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @classmethod
    @abstractmethod
    def new_product(cls, dict_of_product):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        pass


