import pickle




class Cashregister:
    def __init__(self,description=None):
        self._description = description

    def look_up(self, my_items):
        description = str(input('Enter your item: '))
        message = my_items.get(description)
        print(message)



if __name__ == '__main__':
    