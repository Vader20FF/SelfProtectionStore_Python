from abc import ABC


class Address(ABC):
    def __init__(self, street_name, street_number, apartment_number, city_name, postal_code, country):
        self.street_name = street_name
        self.street_number = street_number
        self.apartment_number = apartment_number
        self.city_name = city_name
        self.postal_code = postal_code
        self.country = country

    # Getters
    def get_street_name(self):
        return self.street_name

    def get_street_number(self):
        return self.street_number

    def get_apartment_number(self):
        return self.apartment_number

    def get_city_name(self):
        return self.city_name

    def get_postal_code(self):
        return self.postal_code

    def get_country(self):
        return self.country

    # Others
    def get_address_info(self):
        return f"STREET NAME: {self.get_street_name()}\n" \
               f"STREET NUMBER: {self.get_street_number()}\n" \
               f"APARTMENT NUMBER: {self.get_apartment_number()}\n" \
               f"CITY NAME: {self.get_city_name()}\n" \
               f"POSTAL CODE: {self.get_postal_code()}\n" \
               f"COUNTRY: {self.get_country()}\n"
