class ShoppingCart:
    def __init__(self):
        self.__shopping_cart_total_cost = 0
        self.__shopping_cart_products_list = []

    # Getters
    def get_shopping_cart_total_cost(self):
        return self.__shopping_cart_total_cost

    def get_shopping_cart_products_list(self):
        return self.__shopping_cart_products_list

    # Others
    def get_shopping_cart_info(self):
        summary = ""
        for product in self.get_shopping_cart_products_list():
            summary += product.get_product_info() + '\n'
        summary += f'TOTAL COST: {self.get_shopping_cart_total_cost()}'

    def add_product_to_shopping_cart(self, product):
        self.get_shopping_cart_products_list().append(product)

    def remove_product_from_shopping_cart(self, product):
        self.get_shopping_cart_products_list().remove(product)

    def make_shopping_cart_empty(self):
        self.get_shopping_cart_products_list().clear()
