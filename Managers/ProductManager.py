class ProductManager:
    __products_list = []

    def get_products_list(self):
        """Getting list of existing products"""
        return self.__products_list

    def register_product(self, new_product):
        """Adding a product to products list only if there is no product of given product number"""
        for product in self.get_products_list():
            if product.get_product_number() == new_product.get_product_number():
                # print("\Product of given number already exists!\n")
                return False
        self.get_products_list().append(new_product)
        return True

    def unregister_product(self, product):
        """Removing product from products list"""
        self.get_products_list().remove(product)

    def product_exists(self, product_number):
        """Checking if product already exists in products list by checking product number of every product"""
        for product in self.get_products_list():
            if product_number == product.get_product_number():
                return True
        return False

    def find_all_products(self, search_parameter):
        """Finding all products in products list which get_product_info() method contains given search parameter"""
        results = []
        for product in self.get_products_list():
            if search_parameter in product.get_product_info():
                results.append(product)
        return results

    def find_product(self, search_parameter):
        """Finding first product in products list which get_product_info() method contains given search parameter"""
        for product in self.get_products_list():
            if search_parameter in product.get_product_info():
                return product

    def report(self):
        """Getting info about all products in products list by invoking every product's get_product_info() method"""
        result = ""
        for product in self.get_products_list():
            result = result + product.get_product_info()
        return result

    def get_products_list_size(self):
        """Getting how many products already exist in products list"""
        return len(self.get_products_list())
