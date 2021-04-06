from unittest import TestCase
from Product.ColdSteel.Knife import Knife
from Product.ColdSteel.Machete import Machete
from Product.ColdSteel.Sword import Sword
from Product.Gun.HandGun import HandGun
from Product.Gun.MachineGun import MachineGun
from Product.Gun.PelletGun import PelletGun
from Product.Gun.Shotgun import Shotgun


class TestProduct(TestCase):
    def setUp(self):
        self.knife = Knife(23, "knife_manufacturer", "knife_name", 500, "knife_material", 20)
        self.machete = Machete(23, "machete_manufacturer", "machete_name", 500, "machete_material", "machete_color")
        self.sword = Sword(23, "sword_manufacturer", "sword_name", 500, "sword_material", 30)
        self.handgun = HandGun(23, "handgun_manufacturer", "handgun_name", 500, 30, ".30", "handgun_color")
        self.machinegun = MachineGun(23, "machinegun_manufacturer", "machinegun_name", 500, 30, ".30", "machinegun_fire_mode")
        self.pelletgun = PelletGun(23, "pelletgun_manufacturer", "pelletgun_name", 500, 30, ".30", "pelletgun_fire_rate")
        self.shotgun = Shotgun(23, "shotgun_manufacturer", "shotgun_name", 500, 30, "shotgun_mechanism",
                               40)

    def test_getter_and_setter_knife(self):
        self.knife.set_product_number(50)
        self.assertEqual(self.knife.get_product_number(), 50)

        self.knife.set_manufacturer("nowy_manufacturer")
        self.assertEqual(self.knife.get_manufacturer(), "nowy_manufacturer")

        self.knife.set_product_name("nowy_product_name")
        self.assertEqual(self.knife.get_product_name(), "nowy_product_name")

        self.knife.set_price(300)
        self.assertEqual(self.knife.get_price(), 300)

        self.knife.set_material("nowy_material")
        self.assertEqual(self.knife.get_material(), "nowy_material")

        self.knife.set_weight(10)
        self.assertEqual(self.knife.get_weight(), 10)

        # print()
        # print(self.knife.get_product_info())
        # print()

    def test_getter_and_setter_machete(self):
        self.machete.set_product_number(50)
        self.assertEqual(self.machete.get_product_number(), 50)

        self.machete.set_manufacturer("nowy_manufacturer")
        self.assertEqual(self.machete.get_manufacturer(), "nowy_manufacturer")

        self.machete.set_product_name("nowy_product_name")
        self.assertEqual(self.machete.get_product_name(), "nowy_product_name")

        self.machete.set_price(300)
        self.assertEqual(self.machete.get_price(), 300)

        self.machete.set_material("nowy_material")
        self.assertEqual(self.machete.get_material(), "nowy_material")

        self.machete.set_color("new_color")
        self.assertEqual(self.machete.get_color(), "new_color")

        # print()
        # print(self.machete.get_product_info())
        # print()

    def test_getter_and_setter_sword(self):
        self.sword.set_product_number(50)
        self.assertEqual(self.sword.get_product_number(), 50)

        self.sword.set_manufacturer("nowy_manufacturer")
        self.assertEqual(self.sword.get_manufacturer(), "nowy_manufacturer")

        self.sword.set_product_name("nowy_product_name")
        self.assertEqual(self.sword.get_product_name(), "nowy_product_name")

        self.sword.set_price(300)
        self.assertEqual(self.sword.get_price(), 300)

        self.sword.set_material("nowy_material")
        self.assertEqual(self.sword.get_material(), "nowy_material")

        self.sword.set_length(10)
        self.assertEqual(self.sword.get_length(), 10)

        # print()
        # print(self.sword.get_product_info())
        # print()

    def test_getter_and_setter_handgun(self):
        self.handgun.set_product_number(50)
        self.assertEqual(self.handgun.get_product_number(), 50)

        self.handgun.set_manufacturer("nowy_manufacturer")
        self.assertEqual(self.handgun.get_manufacturer(), "nowy_manufacturer")

        self.handgun.set_product_name("nowy_product_name")
        self.assertEqual(self.handgun.get_product_name(), "nowy_product_name")

        self.handgun.set_price(300)
        self.assertEqual(self.handgun.get_price(), 300)

        self.handgun.set_magazine_capacity(40)
        self.assertEqual(self.handgun.get_magazine_capacity(), 40)

        self.handgun.set_caliber(".81")
        self.assertEqual(self.handgun.get_caliber(), ".81")

        self.handgun.set_color("czerwony")
        self.assertEqual(self.handgun.get_color(), "czerwony")

        # print()
        # print(self.handgun.get_product_info())
        # print()

    def test_getter_and_setter_machinegun(self):
        self.machinegun.set_product_number(50)
        self.assertEqual(self.machinegun.get_product_number(), 50)

        self.machinegun.set_manufacturer("nowy_manufacturer")
        self.assertEqual(self.machinegun.get_manufacturer(), "nowy_manufacturer")

        self.machinegun.set_product_name("nowy_product_name")
        self.assertEqual(self.machinegun.get_product_name(), "nowy_product_name")

        self.machinegun.set_price(300)
        self.assertEqual(self.machinegun.get_price(), 300)

        self.machinegun.set_magazine_capacity(40)
        self.assertEqual(self.machinegun.get_magazine_capacity(), 40)

        self.machinegun.set_caliber(".81")
        self.assertEqual(self.machinegun.get_caliber(), ".81")

        self.machinegun.set_fire_mode("nowy_fire_mode")
        self.assertEqual(self.machinegun.get_fire_mode(), "nowy_fire_mode")

        # print()
        # print(self.machinegun.get_product_info())
        # print()

    def test_getter_and_setter_pelletgun(self):
        self.pelletgun.set_product_number(50)
        self.assertEqual(self.pelletgun.get_product_number(), 50)

        self.pelletgun.set_manufacturer("nowy_manufacturer")
        self.assertEqual(self.pelletgun.get_manufacturer(), "nowy_manufacturer")

        self.pelletgun.set_product_name("nowy_product_name")
        self.assertEqual(self.pelletgun.get_product_name(), "nowy_product_name")

        self.pelletgun.set_price(300)
        self.assertEqual(self.pelletgun.get_price(), 300)

        self.pelletgun.set_magazine_capacity(40)
        self.assertEqual(self.pelletgun.get_magazine_capacity(), 40)

        self.pelletgun.set_caliber(".81")
        self.assertEqual(self.pelletgun.get_caliber(), ".81")

        self.pelletgun.set_fire_rate("new_fire_rate")
        self.assertEqual(self.pelletgun.get_fire_rate(), "new_fire_rate")

        # print()
        # print(self.pelletgun.get_product_info())
        # print()

    def test_getter_and_setter_shotgun(self):
        self.shotgun.set_product_number(50)
        self.assertEqual(self.shotgun.get_product_number(), 50)

        self.shotgun.set_manufacturer("nowy_manufacturer")
        self.assertEqual(self.shotgun.get_manufacturer(), "nowy_manufacturer")

        self.shotgun.set_product_name("nowy_product_name")
        self.assertEqual(self.shotgun.get_product_name(), "nowy_product_name")

        self.shotgun.set_price(300)
        self.assertEqual(self.shotgun.get_price(), 300)

        self.shotgun.set_magazine_capacity(40)
        self.assertEqual(self.shotgun.get_magazine_capacity(), 40)

        self.shotgun.set_mechanism("new_mechanism")
        self.assertEqual(self.shotgun.get_mechanism(), "new_mechanism")

        self.shotgun.set_initial_bullet_velocity(50)
        self.assertEqual(self.shotgun.get_initial_bullet_velocity(), 50)

        # print()
        # print(self.shotgun.get_product_info())
        # print()


