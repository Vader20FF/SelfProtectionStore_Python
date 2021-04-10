from unittest import TestCase
from Product.ColdSteel.Knife import Knife
from Product.ColdSteel.Machete import Machete
from Product.Gun.PelletGun import PelletGun
from Order.ShoppingCart import ShoppingCart


class TestShoppingCart(TestCase):
    def setUp(self):
        self.knife = Knife(23, "knife_manufacturer", "knife_name", 500, "knife_material", 20)
        self.machete = Machete(23, "machete_manufacturer", "machete_name", 500, "machete_material", "machete_color")
        self.pelletgun = PelletGun(23, "pelletgun_manufacturer", "pelletgun_name", 500, 30, ".30",
                                   "pelletgun_fire_rate")
        self.shoppingCart = ShoppingCart()

    def test_add_product_to_shopping_cart(self):
        self.shoppingCart.add_product_to_shopping_cart(self.knife)
        self.assertEqual(len(self.shoppingCart.get_shopping_cart_products_list()), 1)

    def test_remove_product_from_shopping_cart(self):
        self.shoppingCart.add_product_to_shopping_cart(self.knife)
        self.shoppingCart.remove_product_from_shopping_cart(self.knife)
        self.assertEqual(len(self.shoppingCart.get_shopping_cart_products_list()), 0)

    def test_make_shopping_cart_empty(self):
        self.shoppingCart.add_product_to_shopping_cart(self.knife)
        self.shoppingCart.add_product_to_shopping_cart(self.machete)
        self.shoppingCart.add_product_to_shopping_cart(self.pelletgun)
        self.shoppingCart.make_shopping_cart_empty()
        self.assertEqual(len(self.shoppingCart.get_shopping_cart_products_list()), 0)

    def test_get_shopping_cart_total_cost(self):
        self.shoppingCart.add_product_to_shopping_cart(self.knife)
        self.shoppingCart.add_product_to_shopping_cart(self.machete)
        self.assertEqual(self.shoppingCart.get_shopping_cart_total_cost(), 1000)

    def test_shopping_cart_products_list(self):
        self.shoppingCart.add_product_to_shopping_cart(self.knife)
        self.shoppingCart.add_product_to_shopping_cart(self.machete)
        self.shoppingCart.add_product_to_shopping_cart(self.pelletgun)
        self.assertEqual(self.shoppingCart.get_shopping_cart_products_list(),
                         [self.knife, self.machete, self.pelletgun])

        # print()
        # print(self.shoppingCart.get_shopping_cart_info())
        # print()





