class Realitem:
    def __init__(self, description=None, stock=None, price=None):
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
        return "Description : " + self._description + "\n" + "Price : " + str(self._price) + "\n" + "Stock : " + self._stock

def item_input_for_3():
   item = Realitem()
   list_items = []
   for person_num in range(0, 3):
      item.input_description()
      item.input_stock()
      item.input_price()
      description = item.ret_description()
      stock = item.ret_stock()
      price = item.ret_price()
      items = Realitem(description,stock,price)
      list_items.append(items)
   return list_items


def item_display_for_3(list_items):
   for item in list_items:
      print()
      print('Description: ', item.ret_description())
      print('In stock: ', item.ret_stock())
      print('Retail price: ', item.ret_price())
      print()