class Client:
    def __init__(self, first_name, last_name, email_address, phone_number, client_address, shipping_address,
                 is_regular_customer, order_price_limit):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email_address = email_address
        self.__phone_number = phone_number
        self.__client_address = client_address
        self.__shipping_address = shipping_address
        self.__is_regular_customer = is_regular_customer
        self.__order_price_limit = order_price_limit

    # Getters
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email_address(self):
        return self.__email_address

    def get_phone_number(self):
        return self.__phone_number

    def get_client_address(self):
        return self.__client_address

    def get_shipping_address(self):
        return self.__shipping_address

    def get_is_regular_customer(self):
        return self.__is_regular_customer

    def get_order_price_limit(self):
        return self.__order_price_limit

    # Setters
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_email_address(self, email_address):
        self.__email_address = email_address

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_client_address(self, client_address):
        self.__client_address = client_address

    def set_shipping_address(self, shipping_address):
        self.__shipping_address = shipping_address

    def set_is_regular_customer(self, is_regular_customer):
        self.__is_regular_customer = is_regular_customer

    def set_order_price_limit(self, order_price_limit):
        self.__order_price_limit = order_price_limit

    # Others
    def get_client_info(self):
        return f"{self.get_first_name()} {self.get_last_name()}\n{self.get_email_address()}\n" \
               f"{self.get_phone_number()}\n\n{self.get_client_address()}\n\n{self.get_shipping_address()}\n\n" \
               f"{self.get_is_regular_customer()}\n{self.get_order_price_limit()}"



