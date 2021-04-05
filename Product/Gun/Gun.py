from Product.Product import Product
from abc import ABC


class Gun(Product):
    __metaclass__ = ABC

    def __init__(self, product_number, manufacturer, product_name, price, magazine_capacity):
        super().__init__(product_number, manufacturer, product_name, price)
        self.__magazine_capacity = magazine_capacity

    # Getters
    def get_magazine_capacity(self):
        return self.__magazine_capacity

    # Setters
    def set_magazine_capacity(self, magazine_capacity):
        self.__magazine_capacity = magazine_capacity

    # Others
    def get_product_info(self):
        return super().get_product_info() + \
               f'MAGAZINE CAPACITY: {self.get_magazine_capacity()}'
