from unittest import TestCase
from Client.Client import Client
from Client.Company import Company
from Client.PrivateEntrepreneur import PrivateEntrepreneur
from Address.ClientAddress import ClientAddress
from Address.ShippingAddress import ShippingAddress
from Managers.ClientManager import ClientManager


class TestClientManager(TestCase):
    def setUp(self):
        self.client_address = ClientAddress("Ulica", "18", "11", "Miasto", "Kod pocztowy", "Polska")
        self.shipping_address = ShippingAddress("Ulica2", '22', '23', "Miasto2", "Kod pocztowy 2", "Anglia")
        self.client = Client("client_imie", "client_nazwisko", "client_email", "client_phone",
                             self.client_address, self.shipping_address, False)
        self.repeated_client = Client("client_imie", "client_nazwisko", "client_email", "client_phone",
                                      self.client_address, self.shipping_address, False)
        self.new_client_client_address = ClientAddress("Ulica", "18", "11", "Miasto4", "Kod pocztowy", "Polska")
        self.new_client_shipping_address = ShippingAddress("Ulica2", '22', '23', "Miasto6", "Kod pocztowy 2", "Anglia")

        self.private_entrepreneur_client_address = ClientAddress("Ulica", "18", "11", "Miasto", "Kod pocztowy",
                                                                 "Polska")
        self.private_entrepreneur_shipping_address = ShippingAddress("Ulica2", '22', '23', "Miasto2", "Kod pocztowy 2",
                                                                     "Anglia")
        self.private_entrepreneur1 = PrivateEntrepreneur("private_entrepreneur_imie1", "private_entrepreneur_nazwisko",
                                                         "private_entrepreneur_email", "private_entrepreneur_phone1",
                                                         self.private_entrepreneur_client_address,
                                                         self.private_entrepreneur_shipping_address, True,
                                                         "private_entrepreneur_nip",
                                                         "private_entrepreneur_headquarter")
        self.private_entrepreneur2 = PrivateEntrepreneur("private_entrepreneur_imie1", "private_entrepreneur_nazwisko",
                                                         "private_entrepreneur_email", "private_entrepreneur_phone2",
                                                         self.private_entrepreneur_client_address,
                                                         self.private_entrepreneur_shipping_address, True,
                                                         "private_entrepreneur_nip",
                                                         "private_entrepreneur_headquarter")
        self.private_entrepreneur3 = PrivateEntrepreneur("private_entrepreneur_imie2", "private_entrepreneur_nazwisko",
                                                         "private_entrepreneur_email", "private_entrepreneur_phone3",
                                                         self.private_entrepreneur_client_address,
                                                         self.private_entrepreneur_shipping_address, True,
                                                         "private_entrepreneur_nip",
                                                         "private_entrepreneur_headquarter")

        self.client_manager = ClientManager()
        self.client_manager.get_client_list().clear()

    def test_register_client(self):
        self.assertTrue(self.client_manager.register_client(self.client))
        self.assertEqual(self.client_manager.get_clients_list_size(), 1)
        self.assertFalse(self.client_manager.register_client(self.repeated_client))
        self.assertEqual(self.client_manager.get_clients_list_size(), 1)

    def test_unregister_client(self):
        self.client_manager.register_client(self.client)
        self.assertEqual(self.client_manager.get_clients_list_size(), 1)
        self.client_manager.unregister_client(self.client)
        self.assertEqual(self.client_manager.get_clients_list_size(), 0)

    def test_client_exists(self):
        self.client_manager.register_client(self.client)
        self.assertEqual(self.client_manager.get_clients_list_size(), 1)
        self.assertTrue(self.client_manager.client_exists("client_phone"))

    def test_find_all_clients(self):
        self.client_manager.register_client(self.private_entrepreneur1)
        self.client_manager.register_client(self.private_entrepreneur2)
        self.client_manager.register_client(self.private_entrepreneur3)
        self.assertEqual(self.client_manager.get_clients_list_size(), 3)
        results = self.client_manager.find_all_clients("private_entrepreneur_imie1")
        self.assertEqual(len(results), 2)

    def test_find_client(self):
        self.client_manager.register_client(self.private_entrepreneur1)
        self.client_manager.register_client(self.private_entrepreneur2)
        self.client_manager.register_client(self.private_entrepreneur3)
        self.assertEqual(self.client_manager.get_clients_list_size(), 3)
        found_client = self.client_manager.find_client("private_entrepreneur_imie1")
        self.assertEqual(found_client.get_first_name(), "private_entrepreneur_imie1")
