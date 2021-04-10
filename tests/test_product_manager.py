from unittest import TestCase
from Product.ColdSteel.Knife import Knife
from Product.ColdSteel.Machete import Machete
from Product.ColdSteel.Sword import Sword
from Product.Gun.HandGun import HandGun
from Product.Gun.MachineGun import MachineGun
from Product.Gun.PelletGun import PelletGun
from Product.Gun.Shotgun import Shotgun
from Managers.ProductManager import ProductManager


class TestProductManager(TestCase):
    def setUp(self):
        self.knife = Knife(23, "knife_manufacturer", "knife_name", 500, "knife_material", 20)
        self.repeated_knife = Knife(23, "knife_manufacturer", "knife_name", 500, "knife_material", 20)
        self.machete = Machete(24, "manufacturer1", "machete_name", 500, "machete_material", "machete_color")
        self.sword = Sword(25, "manufacturer1", "sword_name", 500, "sword_material", 30)
        self.handgun = HandGun(26, "manufacturer2", "handgun_name", 500, 30, ".30", "handgun_color")
        self.machinegun = MachineGun(27, "machinegun_manufacturer", "machinegun_name", 500, 30, ".30",
                                     "machinegun_fire_mode")
        self.pelletgun = PelletGun(28, "pelletgun_manufacturer", "pelletgun_name", 500, 30, ".30",
                                   "pelletgun_fire_rate")
        self.shotgun = Shotgun(29, "shotgun_manufacturer", "shotgun_name", 500, 30, "shotgun_mechanism",
                               40)

        self.product_manager = ProductManager()
        self.product_manager.get_products_list().clear()

    def test_register_product(self):
        self.assertTrue(self.product_manager.register_product(self.knife))
        self.assertEqual(self.product_manager.get_products_list_size(), 1)
        self.assertFalse(self.product_manager.register_product(self.repeated_knife))
        self.assertEqual(self.product_manager.get_products_list_size(), 1)

    def test_unregister_product(self):
        self.product_manager.register_product(self.knife)
        self.assertEqual(self.product_manager.get_products_list_size(), 1)
        self.product_manager.unregister_product(self.knife)
        self.assertEqual(self.product_manager.get_products_list_size(), 0)

    def test_product_exists(self):
        self.product_manager.register_product(self.knife)
        self.assertTrue(self.product_manager.product_exists(23))

    def test_find_all_products(self):
        self.product_manager.register_product(self.machete)
        self.product_manager.register_product(self.sword)
        self.product_manager.register_product(self.handgun)
        self.assertEqual(self.product_manager.get_products_list_size(), 3)
        results = self.product_manager.find_all_products("manufacturer1")
        self.assertEqual(len(results), 2)

    def test_find_product(self):
        self.product_manager.register_product(self.machete)
        self.product_manager.register_product(self.sword)
        self.product_manager.register_product(self.handgun)
        self.assertEqual(self.product_manager.get_products_list_size(), 3)
        found_product = self.product_manager.find_product("manufacturer1")
        self.assertEqual(found_product.get_manufacturer(), "manufacturer1")
