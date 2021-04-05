from RealGun import RealGun


class HandGun(RealGun):
    def __init__(self, product_number, manufacturer, product_name, price, magazine_capacity, caliber, color):
        super().__init__(product_number, manufacturer, product_name, price, magazine_capacity, caliber)
        self.__color = color

    # Getters
    def get_color(self):
        return self.__color

    # Setters
    def set_color(self, color):
        self.__color = color

    # Others
    def get_product_info(self):
        return super().get_product_info() + \
               f'COLOR: {self.get_color()}'
