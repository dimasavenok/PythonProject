from src.Product import Product


class Category:
    category_count = 0
    product_count = 0



    def __init__(self, name:str, description:str, product:list[Product]):
        self.name = name
        self.description = description
        self.__product = product
        Category.category_count += 1
        Category.product_count += len(product)

    @property
    def product(self):
        result = []
        for i in self.__product:
            result.append(f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт.")
        return "\n".join(result)

    def add_product(self, product):
        """ Добавляет продукт в категорию и увеличивает счётчик """
        if isinstance(product, Product):
            self.__product.append(product)
            self.product_count += 1








