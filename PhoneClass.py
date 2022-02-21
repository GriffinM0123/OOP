class Phone:
    def __init__(self, m, o, r):
        self.__manufact = m
        self.__model = o
        self.__retail_price = r

    def set_manufact(self, m):
        self.__manufact = m

    def set_model(self, o):
        self.__model = o

    def set_retail_price(self, r):
        self.__retail_price = r

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price
