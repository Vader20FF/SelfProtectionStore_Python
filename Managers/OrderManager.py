class OrderManager:
    __orders_list = []

    def get_orders_list(self):
        return self.__orders_list

    def register_order(self, new_order):
        for order in self.get_orders_list():
            if order.get_order_id() == new_order.get_order_id():
                # print("\Order of given ID already exists!\n")
                return False
        self.get_orders_list().append(new_order)
        return True

    def cancel_order(self, order):
        self.get_orders_list().remove(order)

    def get_all_client_orders(self, client):
        results = []
        for order in self.get_orders_list():
            if order.get_client() == client:
                results.append(order)
        return results

    def order_exists(self, order_id):
        for order in self.get_orders_list():
            if order_id == order.get_order_id():
                return True
        return False

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
