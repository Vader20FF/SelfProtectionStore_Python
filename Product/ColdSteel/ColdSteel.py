import Product
from abc import ABC


class ColdSteel(Product, metaclass=ABC):
    def __init__(self, material):
        super().__init__()
        self.__material = material

    # Getters
    def get_material(self):
        return self.__material

    # Setters
    def set_material(self, material):
        self.__material = material

    # Others
    def get_address_info(self):
        return super().get_product_info() + \
               f'MATERIAL: {self.get_material()}'
