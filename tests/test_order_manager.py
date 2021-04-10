from unittest import TestCase
from Product.ColdSteel.Knife import Knife
from Product.ColdSteel.Machete import Machete
from Product.Gun.PelletGun import PelletGun
from Order.ShoppingCart import ShoppingCart
from Order.Order import Order
from Client.Client import Client
from Address.ClientAddress import ClientAddress
from Address.ShippingAddress import ShippingAddress
from Managers.OrderManager import OrderManager
import datetime as dt


class TestOrderManager(TestCase):
    def setUp(self):
        self.client_address = ClientAddress("Ulica", "18", "11", "Miasto", "Kod pocztowy", "Polska")
        self.shipping_address = ShippingAddress("Ulica2", '22', '23', "Miasto2", "Kod pocztowy 2", "Anglia")
        self.client = Client("client_imie", "client_nazwisko", "client_email", "client_phone",
                             self.client_address, self.shipping_address, False)
        self.client2 = Client("client_imie2", "client_nazwisko2", "client_email2", "client_phone2",
                              self.client_address, self.shipping_address, True)
        self.knife = Knife(23, "knife_manufacturer", "knife_name", 500, "knife_material", 20)
        self.machete = Machete(23, "machete_manufacturer", "machete_name", 500, "machete_material", "machete_color")
        self.pelletgun = PelletGun(23, "pelletgun_manufacturer", "pelletgun_name", 500, 30, ".30",
                                   "pelletgun_fire_rate")
        self.shoppingCart = ShoppingCart()
        self.shoppingCart.add_product_to_shopping_cart(self.knife)
        self.shoppingCart.add_product_to_shopping_cart(self.machete)
        self.shoppingCart.add_product_to_shopping_cart(self.pelletgun)
        self.order = Order(self.client, self.shoppingCart, "ZA POBRANIEM")
        self.repeated_order = Order(self.client, self.shoppingCart, "PLATNOSC ONLINE")
        self.order_for_same_client1 = Order(self.client, self.shoppingCart, "PLATNOSC ONLINE")
        self.order_for_same_client2 = Order(self.client, self.shoppingCart, "PLATNOSC ONLINE")
        self.order_for_different_client = Order(self.client2, self.shoppingCart, "PLATNOSC ONLINE")

        self.order_manager = OrderManager()
        self.order_manager.get_orders_list().clear()

    def test_register_order(self):
        self.assertTrue(self.order_manager.register_order(self.order))
        self.assertEqual(self.order_manager.get_orders_list_size(), 1)
        self.assertTrue(self.order_manager.register_order(self.repeated_order))
        self.assertEqual(self.order_manager.get_orders_list_size(), 2)

    def test_cancel_order(self):
        self.order_manager.register_order(self.order)
        self.assertEqual(self.order_manager.get_orders_list_size(), 1)
        self.order_manager.cancel_order(self.order)
        self.assertEqual(self.order_manager.get_orders_list_size(), 0)

    def test_get_all_client_orders(self):
        self.order_manager.register_order(self.order_for_same_client1)
        self.order_manager.register_order(self.order_for_same_client2)
        self.order_manager.register_order(self.order_for_different_client)
        self.assertEqual(self.order_manager.get_orders_list_size(), 3)
        results = self.order_manager.get_all_client_orders(self.client)
        self.assertEqual(len(results), 2)

    def test_order_exists(self):
        self.order_manager.register_order(self.order_for_same_client1)
        self.order_manager.register_order(self.order_for_same_client2)
        self.order_manager.register_order(self.order_for_different_client)
        self.assertEqual(self.order_manager.get_orders_list_size(), 3)
        self.assertTrue(self.order_manager.order_exists(self.order_for_same_client1.get_order_id()))
        self.assertFalse(self.order_manager.order_exists(self.order.get_order_id()))

    def test_find_order(self):
        self.order_manager.register_order(self.order_for_same_client1)
        self.order_manager.register_order(self.order_for_same_client2)
        self.order_manager.register_order(self.order_for_different_client)
        self.assertEqual(self.order_manager.get_orders_list_size(), 3)
        found_order = self.order_manager.find_order("client_imie")
        self.assertEqual(found_order.get_client().get_first_name(), "client_imie")
