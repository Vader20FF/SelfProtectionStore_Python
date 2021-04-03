import AirsoftGun


class MachineGun(AirsoftGun):
    def __init__(self, initial_bullet_velocity, mechanism, magazine_capacity):
        super().__init__(mechanism, magazine_capacity)
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
               f'INITIAL BULLET VELOCITY: {self.get_initial_bullet_velocity()}'
