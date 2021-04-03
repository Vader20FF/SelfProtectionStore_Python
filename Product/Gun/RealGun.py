import Gun
from abc import ABC


class RealGun(Gun, metaclass=ABC):
    def __init__(self, caliber, magazine_capacity):
        super().__init__(magazine_capacity)
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
               f'CALIBER: {self.get_caliber()}'
