class OrderManager:
    __orders_list = []

    def get_orders_list(self):
        """Getting list of existing orders"""
        return self.__orders_list

    def register_order(self, new_order):
        """Adding an order to orders list only if there is no order of given orderID"""
        for order in self.get_orders_list():
            if order.get_order_id() == new_order.get_order_id():
                # print("\Order of given ID already exists!\n")
                return False
        self.get_orders_list().append(new_order)
        return True

    def cancel_order(self, order):
        """Removing order from orders list"""
        self.get_orders_list().remove(order)

    def get_all_client_orders(self, client):
        """Getting list of all orders of specific client"""
        results = []
        for order in self.get_orders_list():
            if order.get_client() == client:
                results.append(order)
        return results

    def order_exists(self, order_id):
        """Checking if order already exists in orders list by checking orderID of every order"""
        for order in self.get_orders_list():
            if order_id == order.get_order_id():
                return True
        return False

    def find_order(self, search_parameter):
        """Finding first order in orders list which get_order_info() method contains given search parameter"""
        for order in self.get_orders_list():
            if search_parameter in order.get_order_info():
                return order

    def report(self):
        """Getting info about all orders in orders list by invoking every order's get_order_info() method"""
        result = ""
        for order in self.get_orders_list():
            result = result + order.get_order_info()
        return result

    def get_orders_list_size(self):
        """Getting how many orders already exist in orders list"""
        return len(self.get_orders_list())
