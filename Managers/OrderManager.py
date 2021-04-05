class OrderManager:
    __orders_list = []

    def get_orders_list(self):
        return self.__orders_list

    def register_order(self, order):
        self.get_orders_list().append(order)

    def cancel_order(self, order):
        self.get_orders_list().remove(order)

    def change_client_type(self, client, new_client_type):
        client.set_client_type(new_client_type)

    def get_all_client_orders(self, client):
        results = []
        for order in self.get_orders_list():
            if order.get_client() == client:
                results.append(order)
        return results

    def order_exists(self, search_parameter):
        for order in self.get_orders_list():
            if search_parameter in order.get_order_info():
                return True
        return False

    def find_all_orders(self, search_parameter):
        results = []
        for order in self.get_orders_list():
            if search_parameter in order.get_order_info():
                results.append(order)
        return results

    def find_order(self, search_parameter):
        for order in self.get_orders_list():
            if search_parameter in order.get_order_info():
                return order

    def report(self):
        result = ""
        for order in self.get_orders_list():
            result = result + order.get_order_info()
        return result

    def get_orders_list_size(self):
        return len(self.get_orders_list())
