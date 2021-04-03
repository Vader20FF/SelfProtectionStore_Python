from abc import ABC


class Product(ABC):
    def __init__(self, product_number, manufacturer, product_name, price):
        self.__product_number = product_number
        self.__manufacturer = manufacturer
        self.__product_name = product_name
        self.__price = price

    # Getters
    def get_product_number(self):
        return self.__product_number

    def get_manufacturer(self):
        return self.__manufacturer

    def get_product_name(self):
        return self.__product_name

    def get_price(self):
        return self.__price

    # Setters
    def set_product_number(self, product_number):
        self.__product_number = product_number

    def set_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    def set_product_name(self, product_name):
        self.__product_name = product_name

    def set_price(self, price):
        self.__price = price

    # Others
    def get_product_info(self):
        return f"PRODUCT NUMBER: {self.get_product_number()}\n" \
               f"MANUFACTURER: {self.get_manufacturer()}\n" \
               f"PRODUCT NAME: {self.get_product_name()}\n" \
               f"PRICE: {self.get_price()}\n\n"
