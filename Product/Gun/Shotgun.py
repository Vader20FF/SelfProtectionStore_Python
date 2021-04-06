from Product.Gun.AirsoftGun import AirsoftGun


class Shotgun(AirsoftGun):
    def __init__(self, product_number, manufacturer, product_name, price, magazine_capacity, mechanism,
                 initial_bullet_velocity):
        super().__init__(product_number, manufacturer, product_name, price, magazine_capacity, mechanism)
        self.__initial_bullet_velocity = initial_bullet_velocity

    # Getters
    def get_initial_bullet_velocity(self):
        return self.__initial_bullet_velocity

    # Setters
    def set_initial_bullet_velocity(self, initial_bullet_velocity):
        self.__initial_bullet_velocity = initial_bullet_velocity

    # Others
    def get_product_info(self):
        return super().get_product_info() + \
               f'INITIAL BULLET VELOCITY: {self.get_initial_bullet_velocity()}\n'
