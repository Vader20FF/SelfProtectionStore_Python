import datetime as dt
import uuid


class Order:
    def __init__(self, client, products_list, shipping_method):
        self.__order_id = uuid.uuid4()
        self.__order_date = dt.datetime.today()
        self.__estimated_delivery_date = dt.date(dt.date.today().year, dt.date.today().month, dt.date.today().day + 2)
        self.__client = client
        self.__products_list = products_list
        self.__shipping_method = shipping_method
        self.__total_cost = 0
        self.__status = "PLACED"

    # Getters
    def get_order_id(self):
        return self.__order_id

    def get_order_date(self):
        return self.__order_date

    def get_estimated_delivery_date(self):
        return self.__estimated_delivery_date

    def get_client(self):
        return self.__client

    def get_products_list(self):
        return self.__products_list

    def get_shipping_method(self):
        return self.__shipping_method

    def get_total_cost(self):
        return self.__total_cost

    def get_status(self):
        return self.__status

    # Setters
    def set_total_cost(self, total_cost):
        self.__total_cost = total_cost

    def set_status(self, status):
        self.__status = status

    # Others
    def get_order_info(self):
        return f"ORDER ID: {self.get_order_id()}\n" \
               f"ORDER DATE: {self.get_order_date()}\n" \
               f"ESTIMATED DELIVERY DATE: {self.get_estimated_delivery_date()}\n" \
               f"SHIPPING METHOD:\n{self.get_shipping_method()}\n\n" \
               f"TOTAL COST: {self.get_total_cost()}\n" \
               f"STATUS: {self.get_status()}\n"
