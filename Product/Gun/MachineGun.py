from RealGun import RealGun


class MachineGun(RealGun):
    def __init__(self, product_number, manufacturer, product_name, price, magazine_capacity, caliber, fire_mode):
        super().__init__(product_number, manufacturer, product_name, price, magazine_capacity, caliber)
        self.__fire_mode = fire_mode

    # Getters
    def get_fire_mode(self):
        return self.__fire_mode

    # Setters
    def set_fire_mode(self, fire_mode):
        self.__fire_mode = fire_mode

    # Others
    def get_product_info(self):
        return super().get_product_info() + \
               f'FIRE MODE: {self.get_fire_mode()}'
