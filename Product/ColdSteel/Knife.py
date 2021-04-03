import ColdSteel


class Knife(ColdSteel):
    def __init__(self, weight, material):
        super().__init__(material)
        self.__weight = weight

    # Getters
    def get_weight(self):
        return self.__weight

    # Setters
    def set_weight(self, weight):
        self.__weight = weight

    # Others
    def get_address_info(self):
        return super().get_product_info() + \
               f'WEIGHT: {self.get_weight()}'
