from ColdSteel import ColdSteel


class Knife(ColdSteel):
    def __init__(self, product_number, manufacturer, product_name, price, material, weight):
        super().__init__(product_number, manufacturer, product_name, price, material)
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
