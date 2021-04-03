import RealGun


class MachineGun(RealGun):
    def __init__(self, fire_mode, caliber, magazine_capacity):
        super().__init__(caliber, magazine_capacity)
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
