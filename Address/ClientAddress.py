from Address import Address


class ClientAddress(Address):
    def __init__(self, street_name, street_number, apartment_number, city_name, postal_code, set_country):
        super().__init__(street_name, street_number, apartment_number, city_name, postal_code, set_country)

    # Setters
    def set_street_name(self, street_name):
        super().__street_name = street_name

    def set_street_number(self, street_number):
        super().__street_number = street_number

    def set_apartment_number(self, apartment_number):
        super().__apartment_number = apartment_number

    def set_city_name(self, city_name):
        super().__city_name = city_name

    def set_postal_code(self, postal_code):
        super().__postal_code = postal_code

    def set_country(self, country):
        super().__country = country
