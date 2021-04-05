from unittest import TestCase
from Address.ClientAddress import ClientAddress
from Address.ShippingAddress import ShippingAddress


class TestAddress(TestCase):
    def setUp(self):
        self.client_address = ClientAddress("Ulica", "18", "11", "Miasto", "Kod pocztowy", "Polska")
        self.shipping_address = ShippingAddress("Ulica2", '22', '23', "Miasto2", "Kod pocztowy 2", "Anglia")

    def test_getter_and_setter_client_address(self):
        self.client_address.set_street_name("Nowa_ulica1")
        self.assertEqual(self.client_address.get_street_name(), "Nowa_ulica1")

        self.client_address.set_street_number("22")
        self.assertEqual(self.client_address.get_street_number(), "22")

        self.client_address.set_apartment_number("20")
        self.assertEqual(self.client_address.get_apartment_number(), "20")

        self.client_address.set_city_name("City")
        self.assertEqual(self.client_address.get_city_name(), "City")

        self.client_address.set_postal_code("Kodzik")
        self.assertNotEqual(self.client_address.get_postal_code(), "Kodzik1")

        self.client_address.set_country("Panstwo")
        self.assertEqual(self.client_address.get_country(), "Panstwo")

    def test_getter_and_setter_shipping_address(self):
        self.assertEqual(self.shipping_address.get_street_name(), "Ulica2")
        self.assertEqual(self.shipping_address.get_street_number(), "22")
        self.assertEqual(self.shipping_address.get_apartment_number(), "23")
        self.assertEqual(self.shipping_address.get_city_name(), "Miasto2")
        self.assertEqual(self.shipping_address.get_postal_code(), "Kod pocztowy 2")
        self.assertEqual(self.shipping_address.get_country(), "Anglia")


