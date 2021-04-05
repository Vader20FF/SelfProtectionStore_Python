from Product.ColdSteel import ColdSteel


class Machete(ColdSteel):
    def __init__(self, product_number, manufacturer, product_name, price, material, color):
        super().__init__(product_number, manufacturer, product_name, price, material)
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
