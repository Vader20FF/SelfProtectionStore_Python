from Address.Address import Address


class ShippingAddress(Address):
    def __init__(self, street_name, street_number, apartment_number, city_name, postal_code, set_country):
        super().__init__(street_name, street_number, apartment_number, city_name, postal_code, set_country)
