from Client.Client import Client
from Address.ClientAddress import ClientAddress
from Address.ShippingAddress import ShippingAddress


class ClientManager:
    __clients_list = []

    def get_client_list(self):
        return self.__clients_list

    def register_client(self, new_client):
        for client in self.get_client_list():
            if client.get_phone_number() == new_client.get_phone_number():
                # print("\Client of given phone number already exists!\n")
                return False
        self.get_client_list().append(new_client)
        return True

    def unregister_client(self, client):
        self.get_client_list().remove(client)

    def client_exists(self, client_phone_number):
        for client in self.get_client_list():
            if client_phone_number == client.get_phone_number():
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
