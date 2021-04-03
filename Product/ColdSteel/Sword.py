import ColdSteel


class Sword(ColdSteel):
    def __init__(self, length, material):
        super().__init__(material)
        self.__length = length

    # Getters
    def get_length(self):
        return self.__length

    # Setters
    def set_length(self, length):
        self.__length = length

    # Others
    def get_address_info(self):
        return super().get_product_info() + \
               f'LENGTH: {self.get_length()}'
