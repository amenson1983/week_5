import pickle

from lesson_5_homework.cashregister_class import Cashregister
from lesson_5_homework.realitem_class import item_input_for_3, item_display_for_3

filename = 'supermarket.dat'
quit_ = 5
purchase_ = 1
clear_bin_ = 3
get_total_bin_cost_ = 2
show_stock = 4
bin = []




def get_menu_choice():
    print('_____________________________')
    print('1. Purchase')
    print('2. Get cost of bin')
    print('3. Clear the bin up')
    print('4. Show goods in stock')
    print('5. Quit')
    choice = int(input('Please make a choice: '))
    while choice < purchase_ or choice > quit_:
        choice = int(input('Please make a choice: '))
    return choice


def show_stock_(my_items):
    for i in range(0,len(my_items)):
        print(my_items[i])


def add_to_bin(my_items,bin):
    continue_ = 'y'
    while continue_.lower == 'y':
        description = input('Choose the item to add it to bin: ')
        entry = my_items.get(description)
        if description in my_items:
            bin.append(entry)
            print('Entry has been added')
        continue_ = input('Continue shopping? y/n')
    return bin


def main():
    my_items = load_items()

    choice = 0
    while choice != quit_:
        choice = get_menu_choice()  # меню
        if choice == show_stock:
            show_stock_(my_items)  # показывает ассортимент из списка товаров
        elif choice == purchase_:
            add_to_bin()  # Создает список с выбранными товарами на основе списка товаров возвращает bin
        elif choice == clear_bin_:
            delete_bin(bin)  # очищает список
        elif choice == get_total_bin_cost_:
            get_total_bin_cost(bin)  # возвращает стоимость товаров в корзине
    save_bin(bin)  # сохраняет в файл корзину
    save_my_items(my_items)  # сохраняет в файл корзину


def input_and_save_items():
    my_items = item_input_for_3()
    output_file = open(filename, 'wb')
    pickle.dump(my_items, output_file)
    output_file.close()
    print(my_items)

def load_items(filename):
        try:
            input_file = open(filename, 'rb')
            my_items = pickle.load(input_file)
            input_file.close()
        except IOError:
            my_items = {}
        return my_items


if __name__ == '__main__':
