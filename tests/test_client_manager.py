from unittest import TestCase
from Client.Client import Client
from Client.Company import Company
from Client.PrivateEntrepreneur import PrivateEntrepreneur
from Address.ClientAddress import ClientAddress
from Address.ShippingAddress import ShippingAddress


class TestClient(TestCase):
    def setUp(self):
        self.client_address = ClientAddress("Ulica", "18", "11", "Miasto", "Kod pocztowy", "Polska")
        self.shipping_address = ShippingAddress("Ulica2", '22', '23', "Miasto2", "Kod pocztowy 2", "Anglia")
        self.client = Client("client_imie", "client_nazwisko", "client_email", "client_phone",
                             self.client_address, self.shipping_address, False, 400)
        self.new_client_client_address = ClientAddress("Ulica", "18", "11", "Miasto4", "Kod pocztowy", "Polska")
        self.new_client_shipping_address = ShippingAddress("Ulica2", '22', '23', "Miasto6", "Kod pocztowy 2", "Anglia")

        self.company_client_address = ClientAddress("Ulica", "18", "11", "Miasto", "Kod pocztowy", "Polska")
        self.company_shipping_address = ShippingAddress("Ulica2", '22', '23', "Miasto2", "Kod pocztowy 2", "Anglia")
        self.company = Company("company_imie", "company_nazwisko", "company_email", "company_phone",
                               self.company_client_address, self.company_shipping_address, True, 500, "company_nip",
                               "company_headquarter")
        self.new_company_client_address = ClientAddress("Ulica", "18", "11", "Miasto4", "Kod pocztowy", "Polska")
        self.new_company_shipping_address = ShippingAddress("Ulica2", '22', '23', "Miasto6", "Kod pocztowy 2", "Anglia")

        self.private_entrepreneur_client_address = ClientAddress("Ulica", "18", "11", "Miasto", "Kod pocztowy",
                                                                 "Polska")
        self.private_entrepreneur_shipping_address = ShippingAddress("Ulica2", '22', '23', "Miasto2", "Kod pocztowy 2",
                                                                     "Anglia")
        self.private_entrepreneur = PrivateEntrepreneur("private_entrepreneur_imie", "private_entrepreneur_nazwisko",
                                                        "private_entrepreneur_email", "private_entrepreneur_phone",
                                                        self.private_entrepreneur_client_address,
                                                        self.private_entrepreneur_shipping_address, True, 300,
                                                        "private_entrepreneur_nip",
                                                        "private_entrepreneur_headquarter")
        self.new_private_entrepreneur_client_address = ClientAddress("Ulica", "18", "11", "Miasto4", "Kod pocztowy", "Polska")
        self.new_private_entrepreneur_shipping_address = ShippingAddress("Ulica2", '22', '23', "Miasto6", "Kod pocztowy 2", "Anglia")

    def test_register_client(self):
        pass

    def test_client_exists(self):
        pass

    def test_find_all_clients(self):
        pass

    def test_find_client(self):
        pass

    def test_get_clients_list_size(self):
        pass


