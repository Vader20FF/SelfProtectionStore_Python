class ProductManager:
    __products_list = []

    def get_products_list(self):
        return self.__products_list

    def register_product(self, new_product):
        for product in self.get_products_list():
            if product.get_product_number() == new_product.get_product_number():
                # print("\Product of given number already exists!\n")
                return False
        self.get_products_list().append(new_product)
        return True

    def unregister_product(self, product):
        self.get_products_list().remove(product)

    def product_exists(self, product_number):
        for product in self.get_products_list():
            if product_number == product.get_product_number():
                return True
        return False

    def find_all_products(self, search_parameter):
        results = []
        for product in self.get_products_list():
            if search_parameter in product.get_product_info():
                results.append(product)
        return results

    def find_product(self, search_parameter):
        for product in self.get_products_list():
            if search_parameter in product.get_product_info():
                return product

    def report(self):
        result = ""
        for product in self.get_products_list():
            result = result + product.get_product_info()
        return result

    def get_products_list_size(self):
        return len(self.get_products_list())
