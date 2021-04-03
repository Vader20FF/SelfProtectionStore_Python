import RealGun


class HandGun(RealGun):
    def __init__(self, color, caliber, magazine_capacity):
        super().__init__(caliber, magazine_capacity)
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
