from RealGun import RealGun


class PelletGun(RealGun):
    def __init__(self, product_number, manufacturer, product_name, price, magazine_capacity, caliber, fire_rate):
        super().__init__(product_number, manufacturer, product_name, price, magazine_capacity, caliber)
        self.__fire_rate = fire_rate

    # Getters
    def get_fire_rate(self):
        return self.__fire_rate

    # Setters
    def set_fire_rate(self, fire_rate):
        self.__fire_rate = fire_rate

    # Others
    def get_product_info(self):
        return super().get_product_info() + \
               f'FIRE RATE: {self.get_fire_rate()}'
