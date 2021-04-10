from unittest import TestCase
from Product.ColdSteel.Knife import Knife
from Product.ColdSteel.Machete import Machete
from Product.Gun.PelletGun import PelletGun
from Order.ShoppingCart import ShoppingCart
from Order.Order import Order
from Client.Client import Client
from Address.ClientAddress import ClientAddress
from Address.ShippingAddress import ShippingAddress
import datetime as dt


class TestOrder(TestCase):
    def setUp(self):
        self.client_address = ClientAddress("Ulica", "18", "11", "Miasto", "Kod pocztowy", "Polska")
        self.shipping_address = ShippingAddress("Ulica2", '22', '23', "Miasto2", "Kod pocztowy 2", "Anglia")
        self.client = Client("client_imie", "client_nazwisko", "client_email", "client_phone",
                             self.client_address, self.shipping_address, False)
        self.knife = Knife(23, "knife_manufacturer", "knife_name", 500, "knife_material", 20)
        self.machete = Machete(23, "machete_manufacturer", "machete_name", 500, "machete_material", "machete_color")
        self.pelletgun = PelletGun(23, "pelletgun_manufacturer", "pelletgun_name", 500, 30, ".30",
                                   "pelletgun_fire_rate")
        self.shoppingCart = ShoppingCart()
        self.shoppingCart.add_product_to_shopping_cart(self.knife)
        self.shoppingCart.add_product_to_shopping_cart(self.machete)
        self.shoppingCart.add_product_to_shopping_cart(self.pelletgun)
        self.order = Order(self.client, self.shoppingCart, "ZA POBRANIEM")

    def test_getter_and_setter(self):
        self.order.set_status("WYSLANE")
        self.assertEqual(self.order.get_status(), "WYSLANE")

        self.assertEqual(self.order.get_order_date(), dt.datetime.today())

        self.assertEqual(self.order.get_estimated_delivery_date(),
                         dt.date(dt.date.today().year, dt.date.today().month, dt.date.today().day + 2))

        self.assertEqual(self.order.get_client(), self.client)

        self.assertEqual(self.order.get_shopping_cart(), self.shoppingCart)

        self.assertEqual(self.order.get_shipping_method(), "ZA POBRANIEM")

        self.assertEqual(self.order.get_total_cost(), 1500)

        # print()
        # print(self.order.get_order_info())
        # print()
