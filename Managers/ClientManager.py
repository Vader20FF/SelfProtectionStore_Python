from Client.Client import Client
from Address.ClientAddress import ClientAddress
from Address.ShippingAddress import ShippingAddress


class ClientManager:
    __clients_list = []

    def get_client_list(self):
        return self.__clients_list

    def register_client(self, first_name, last_name, email_address, phone_number,
                        client_street_name, client_street_number, client_apartment_number, client_city_name,
                        client_postal_code, client_country,
                        shipping_street_name, shipping_street_number, shipping_apartment_number, shipping_city_name,
                        shipping_postal_code, shipping_country,
                        is_regular_customer):
        client_address = ClientAddress(client_street_name, client_street_number, client_apartment_number,
                                       client_city_name, client_postal_code, client_country)
        shipping_address = ShippingAddress(shipping_street_name, shipping_street_number, shipping_apartment_number,
                                           shipping_city_name, shipping_postal_code, shipping_country)
        new_client = Client(first_name, last_name, email_address, phone_number, client_address, shipping_address,
                            is_regular_customer)
        for client in self.get_client_list():
            if client.get_phone_number() == phone_number:
                print("\nUser of such phone number already exists!\n")
                return False
        self.get_client_list().append(new_client)
        return True

    def unregister_client(self, client):
        self.get_client_list().remove(client)

    def client_exists(self, search_parameter):
        for client in self.get_client_list():
            if search_parameter in client.get_client_info():
                return True
        return False

    def find_all_clients(self, search_parameter):
        results = []
        for client in self.get_client_list():
            if search_parameter in client.get_client_info():
                results.append(client)
        return results

    def find_client(self, search_parameter):
        for client in self.get_client_list():
            if search_parameter in client.get_client_info():
                return client

    def report(self):
        result = ""
        for client in self.get_client_list():
            result = result + client.get_client_info()
        return result

    def get_clients_list_size(self):
        return len(self.get_client_list())
