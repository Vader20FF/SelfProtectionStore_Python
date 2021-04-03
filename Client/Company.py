import Entrepreneur


class Company(Entrepreneur):
    def __init__(self, headquarter_city, nip):
        super().__init__(nip)
        self.__headquarter_city = headquarter_city

    def get_headquarter_city(self):
        return self.__headquarter_city

    def set_headquarter_city(self, headquarter_city):
        self.__headquarter_city = headquarter_city

    def get_client_info(self):
        return super().get_client_info() + \
               f'HEADQUARTER CITY: {self.get_headquarter_city()}\n\n'

