import unittest
from ClientAddress import ClientAddress
from ShippingAddress import ShippingAddress


class MyTestCase(unittest.TestCase):
    client_address = ClientAddress("Ulica", "18", "11", "Miasto", "Kod pocztowy", "Polska")
    shipping_address = ShippingAddress("Ulica2", '22', '23', "Miasto2", "Kod pocztowy 2", "Anglia")

    def getter_and_setter_tests_client_address(self):
        self.client_address.set_street_name("Nowa_ulica")
        self.assertEqual(self.client_address.get_street_name(), "Nowa_ulica")

        self.client_address.set_street_number("22")
        self.assertEqual(self.client_address.get_street_name(), "22")

        self.client_address.set_apartment_number("20")
        self.assertEqual(self.client_address.get_street_name(), "20")

        self.client_address.set_city_name("City")
        self.assertEqual(self.client_address.get_street_name(), "City")

        self.client_address.set_postal_code("Kodzik")
        self.assertEqual(self.client_address.get_street_name(), "Kodzik")

        self.client_address.set_country("Panstwo")
        self.assertEqual(self.client_address.get_street_name(), "Panstwo")

    def getter_and_setter_tests_shipping_address(self):
        self.shipping_address.set_street_name("Nowa_ulica2")
        self.assertEqual(self.shipping_address.get_street_name(), "Nowa_ulica")

        self.shipping_address.set_street_number("2252")
        self.assertEqual(self.shipping_address.get_street_name(), "2252")

        self.shipping_address.set_apartment_number("22234")
        self.assertEqual(self.shipping_address.get_street_name(), "22234")

        self.shipping_address.set_city_name("Cit2y")
        self.assertEqual(self.shipping_address.get_street_name(), "Cit2y")

        self.shipping_address.set_postal_code("Kodzik2")
        self.assertEqual(self.shipping_address.get_street_name(), "Kodzik2")

        self.shipping_address.set_country("Panstw23o")
        self.assertEqual(self.shipping_address.get_street_name(), "Panstw23o")


