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

    def test_getter_and_setter_client(self):
        self.client.set_first_name("nowe_imie")
        self.assertEqual(self.client.get_first_name(), "nowe_imie")

        self.client.set_last_name("nowe_nazwisko")
        self.assertEqual(self.client.get_last_name(), "nowe_nazwisko")

        self.client.set_email_address("nowy_email")
        self.assertEqual(self.client.get_email_address(), "nowy_email")

        self.client.set_phone_number("nowy_phone")
        self.assertEqual(self.client.get_phone_number(), "nowy_phone")

        self.client.set_client_address(self.new_client_client_address)
        self.assertEqual(self.client.get_client_address(), self.new_client_client_address)

        self.client.set_shipping_address(self.new_client_shipping_address)
        self.assertEqual(self.client.get_shipping_address(), self.new_client_shipping_address)

        self.client.set_is_regular_customer(True)
        self.assertEqual(self.client.get_is_regular_customer(), True)

        self.client.set_order_price_limit(1000)
        self.assertEqual(self.client.get_order_price_limit(), 1000)

    def test_getter_and_setter_company(self):
        self.company.set_first_name("nowe_imie")
        self.assertEqual(self.company.get_first_name(), "nowe_imie")

        self.company.set_last_name("nowe_nazwisko")
        self.assertEqual(self.company.get_last_name(), "nowe_nazwisko")

        self.company.set_email_address("nowy_email")
        self.assertEqual(self.company.get_email_address(), "nowy_email")

        self.company.set_phone_number("nowy_phone")
        self.assertEqual(self.company.get_phone_number(), "nowy_phone")

        self.company.set_client_address(self.new_company_client_address)
        self.assertEqual(self.company.get_client_address(), self.new_company_client_address)

        self.company.set_shipping_address(self.new_company_shipping_address)
        self.assertEqual(self.company.get_shipping_address(), self.new_company_shipping_address)

        self.company.set_is_regular_customer(False)
        self.assertEqual(self.company.get_is_regular_customer(), False)

        self.company.set_order_price_limit(1000)
        self.assertEqual(self.company.get_order_price_limit(), 1000)

        self.company.set_nip("nowy_nip")
        self.assertEqual(self.company.get_nip(), "nowy_nip")

    def test_getter_and_setter_private_entrepreneur(self):
        self.private_entrepreneur.set_first_name("nowe_imie")
        self.assertEqual(self.private_entrepreneur.get_first_name(), "nowe_imie")

        self.private_entrepreneur.set_last_name("nowe_nazwisko")
        self.assertEqual(self.private_entrepreneur.get_last_name(), "nowe_nazwisko")

        self.private_entrepreneur.set_email_address("nowy_email")
        self.assertEqual(self.private_entrepreneur.get_email_address(), "nowy_email")

        self.private_entrepreneur.set_phone_number("nowy_phone")
        self.assertEqual(self.private_entrepreneur.get_phone_number(), "nowy_phone")

        self.private_entrepreneur.set_client_address(self.new_private_entrepreneur_client_address)
        self.assertEqual(self.private_entrepreneur.get_client_address(), self.new_private_entrepreneur_client_address)

        self.private_entrepreneur.set_shipping_address(self.new_private_entrepreneur_shipping_address)
        self.assertEqual(self.private_entrepreneur.get_shipping_address(),
                         self.new_private_entrepreneur_shipping_address)

        self.private_entrepreneur.set_is_regular_customer(False)
        self.assertEqual(self.private_entrepreneur.get_is_regular_customer(), False)

        self.private_entrepreneur.set_order_price_limit(1000)
        self.assertEqual(self.private_entrepreneur.get_order_price_limit(), 1000)

        self.company.set_headquarter_city("nowy_headquarter")
        self.assertEqual(self.company.get_headquarter_city(), "nowy_headquarter")

