class ClientManager:
    __clients_list = []

    def get_client_list(self):
        """Getting list of existing clients"""
        return self.__clients_list

    def register_client(self, new_client):
        """Adding a client to clients list only if there is no user of given phone number"""
        for client in self.get_client_list():
            if client.get_phone_number() == new_client.get_phone_number():
                # print("\Client of given phone number already exists!\n")
                return False
        self.get_client_list().append(new_client)
        return True

    def unregister_client(self, client):
        """Removing client from clients list"""
        self.get_client_list().remove(client)

    def client_exists(self, client_phone_number):
        """Checking if client already exists in clients list by checking phone number of every client"""
        for client in self.get_client_list():
            if client_phone_number == client.get_phone_number():
                return True
        return False

    def find_all_clients(self, search_parameter):
        """Finding all clients in clients list which get_client_info() method contains given search parameter"""
        results = []
        for client in self.get_client_list():
            if search_parameter in client.get_client_info():
                results.append(client)
        return results

    def find_client(self, search_parameter):
        """Finding first client in clients list which get_client_info() method contains given search parameter"""
        for client in self.get_client_list():
            if search_parameter in client.get_client_info():
                return client

    def report(self):
        """Getting info about all clients in clients list by invoking every client's get_client_info() method"""
        result = ""
        for client in self.get_client_list():
            result = result + client.get_client_info()
        return result

    def get_clients_list_size(self):
        """Getting how many clients already exist in clients list"""
        return len(self.get_client_list())
