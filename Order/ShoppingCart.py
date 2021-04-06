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
        summary = "Shopping Cart:\n\n"
        for product in self.get_shopping_cart_products_list():
            summary += f'{product.get_product_info()}\n'
        summary += f'\nTOTAL COST: {self.get_shopping_cart_total_cost()}'
        return summary

    def add_product_to_shopping_cart(self, product):
        self.__shopping_cart_products_list.append(product)
        self.__shopping_cart_total_cost += product.get_price()

    def remove_product_from_shopping_cart(self, product):
        self.__shopping_cart_products_list.remove(product)

    def make_shopping_cart_empty(self):
        self.__shopping_cart_products_list.clear()
