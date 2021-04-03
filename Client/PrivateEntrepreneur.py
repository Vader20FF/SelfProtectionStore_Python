import Entrepreneur


class PrivateEntrepreneur(Entrepreneur):
    def __init__(self, vat_payer):
        super().__init__()
        self.__vat_payer = vat_payer

    def get_vat_payer(self):
        return self.__vat_payer

    def set_vat_payer(self, vat_payer):
        self.__vat_payer = vat_payer

    def get_client_info(self):
        return super().get_client_info() + \
               f'VAT PAYER: {self.get_vat_payer()}\n'
