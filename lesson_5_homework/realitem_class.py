class Realitem:
    def __init__(self, description=None, stock=None, price=None, phone=None):
        self._description = description
        self._stock = stock
        self._price = price


    def input_description(self):
        description = input('Input description: ')
        self._description = description

    def input_stock(self):
        stock = input('Input stock: ')
        self._stock = stock

    def input_price(self):
        price = input('Input price: ')
        self._price = price


    def ret_description(self):
        return self._description

    def ret_stock(self):
        return self._stock

    def ret_price(self):
        return self._price



    def __str__(self):
        return "Description : " + self._description + "\n" + "Age : " + str(self._price) + "\n" + "Adress : " + self._stock
