from Product.Gun.Gun import Gun
from abc import ABC


class RealGun(Gun):
    __metaclass__ = ABC

    def __init__(self, product_number, manufacturer, product_name, price, magazine_capacity, caliber):
        super().__init__(product_number, manufacturer, product_name, price, magazine_capacity)
        self.__caliber = caliber

    # Getters
    def get_caliber(self):
        return self.__caliber

    # Setters
    def set_caliber(self, caliber):
        self.__caliber = caliber

    # Others
    def get_product_info(self):
        return super().get_product_info() + \
               f'CALIBER: {self.get_caliber()}\n'
