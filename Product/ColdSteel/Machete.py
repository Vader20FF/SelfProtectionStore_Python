import ColdSteel


class Machete(ColdSteel):
    def __init__(self, color, material):
        super().__init__(material)
        self.__color = color

    # Getters
    def get_color(self):
        return self.__color

    # Setters
    def set_color(self, color):
        self.__color = color

    # Others
    def get_address_info(self):
        return super().get_product_info() + \
               f'COLOR: {self.get_color()}'
