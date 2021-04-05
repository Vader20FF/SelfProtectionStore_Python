from Client.Entrepreneur import Entrepreneur


class Company(Entrepreneur):
    def __init__(self, first_name, last_name, email_address, phone_number, client_address, shipping_address,
                 is_regular_customer, order_price_limit, nip, headquarter_city):
        super().__init__(first_name, last_name, email_address, phone_number, client_address, shipping_address,
                         is_regular_customer, order_price_limit, nip)
        self.__headquarter_city = headquarter_city

    def get_headquarter_city(self):
        return self.__headquarter_city

    def set_headquarter_city(self, headquarter_city):
        self.__headquarter_city = headquarter_city

    def get_client_info(self):
        return super().get_client_info() + \
               f'HEADQUARTER CITY: {self.get_headquarter_city()}\n\n'

