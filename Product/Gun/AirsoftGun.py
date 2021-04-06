from Product.Gun.Gun import Gun
from abc import ABC


class AirsoftGun(Gun):
    __metaclass__ = ABC

    def __init__(self, product_number, manufacturer, product_name, price, magazine_capacity, mechanism):
        super().__init__(product_number, manufacturer, product_name, price, magazine_capacity)
        self.__mechanism = mechanism

    # Getters
    def get_mechanism(self):
        return self.__mechanism

    # Setters
    def set_mechanism(self, mechanism):
        self.__mechanism = mechanism

    # Others
    def get_product_info(self):
        return super().get_product_info() + \
               f'MECHANISM: {self.get_mechanism()}\n'
