import pickle


from lesson_5_homework.realitem_class import Realitem
filename = 'bin1.dat'
filename1 = 'sum.dat'

class CashRegister:
    def __init__(self, description=None, quantity=None, price=None):
        self._description = description
        self._quantity = quantity
        self._price = price


    def input_description(self):
        description = input('Input description: ')
        self._description = description

    def input_quantity(self):
        quantity = input('Input stock: ')
        self._quantity = quantity

    def input_price(self):
        price = input('Input price: ')
        self._price = price


    def ret_description(self):
        return self._description

    def ret_quantity(self):
        return self._quantity

    def ret_price(self):
        return self._price

    def get_sum_(self):
        price = self.ret_price
        quantity = self.ret_quantity
        sum = float(price) * float(quantity)
        return sum

def load_items(filename):
    try:
        input_file = open(filename, 'rb')
        my_items = pickle.load(input_file)
        input_file.close()
    except IOError:
        my_items = {}
    return my_items

def load_sum(filename1):
    try:
        input_file = open(filename1, 'rb')
        sum = pickle.load(input_file)
        input_file.close()
    except IOError:
        my_items = {}
    return sum

def get_menu_choice():
    print('_____________________________')
    print('1. Show bin')
    print('2. Choose items to buy')
    print('3. Get the sum to pay')
    print('4. Clear bin')
    print('5. Quit')
    choice = int(input('Please make a choice: '))
    while choice < 1 or choice > 5:
        choice = int(input('Please make a choice: '))
    return choice

def item_input():
   q = int(input('How many items?'))
   item = CashRegister()
   sum = 0
   list_items = {}
   for person_num in range(0, q):
      item.input_description()
      item.input_quantity()
      item.input_price()
      description = item.ret_description()
      quantity = item.ret_quantity()
      price = item.ret_price()
      sum += float(quantity) * float(price)
      items = Realitem(description,quantity,price)
      list_items[description] = items
      print(list_items,sum)
   return list_items, sum


def clear():
    list_items = load_items(filename)
    list_items.clear()
    del list_items


def save_items_to_bin(list_items):
    output_file = open(filename,'wb')
    pickle.dump(list_items, output_file)
    output_file.close()

def save_sum_to_bin(sum):
    output_file = open(filename1,'wb')
    pickle.dump(sum, output_file)
    output_file.close()

def show_bin():
    list_items = load_items(filename)
    print(list_items)