class ClientManager:
    __client_list = []

    def get_client_list(self):
        return self.__client_list

    def register_client(self, client):
        self.get_client_list().append(client)

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
