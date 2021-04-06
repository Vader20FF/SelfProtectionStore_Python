from Client.Client import Client
from abc import ABC


class Entrepreneur(Client):
    __metaclass__ = ABC

    def __init__(self, first_name, last_name, email_address, phone_number, client_address, shipping_address,
                 is_regular_customer, nip):
        super().__init__(first_name, last_name, email_address, phone_number, client_address, shipping_address,
                         is_regular_customer)
        self.__nip = nip

    def get_nip(self):
        return self.__nip

    def set_nip(self, nip):
        self.__nip = nip

    def get_client_info(self):
        return super().get_client_info() + \
               f'NIP: {self.get_nip()}\n'
