import Client
from abc import ABC


class Entrepreneur(Client, metaclass=ABC):
    def __init__(self, nip):
        super().__init__()
        self.__nip = nip

    def get_nip(self):
        return self.__nip

    def set_nip(self, nip):
        self.__nip = nip

    def get_client_info(self):
        return super().get_client_info() + \
               f'NIP: {self.get_nip()}\n'


