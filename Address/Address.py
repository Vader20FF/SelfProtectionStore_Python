from abc import ABC


class Address(ABC):
    def __init__(self, street_name, street_number, apartment_number, city_name, postal_code, country):
        self.__street_name = street_name
        self.__street_number = street_number
        self.__apartment_number = apartment_number
        self.__city_name = city_name
        self.__postal_code = postal_code
        self.__country = country

    # Getters
    def get_street_name(self):
        return self.__street_name

    def get_street_number(self):
        return self.__street_number

    def get_apartment_number(self):
        return self.__apartment_number

    def get_city_name(self):
        return self.__city_name

    def get_postal_code(self):
        return self.__postal_code

    def get_country(self):
        return self.__country

    # Others
    def get_address_info(self):
        return f"STREET NAME: {self.get_street_name()}\n" \
               f"STREET NUMBER: {self.get_street_number()}\n" \
               f"APARTMENT NUMBER: {self.get_apartment_number()}\n" \
               f"CITY NAME: {self.get_city_name()}\n\n" \
               f"POSTAL CODE:\n{self.get_postal_code()}\n\n" \
               f"COUNTRY:\n{self.get_country()}\n\n"
