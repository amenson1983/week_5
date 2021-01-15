from lesson_5_homework.cashregister_class_1 import load_items, get_menu_choice, show_bin, item_input, clear, \
    save_items_to_bin, CashRegister, load_sum, save_sum_to_bin
import pickle

show_ = 1
choose_ = 2
get_sum = 3
clear_ = 4
quit_ = 5
filename = 'bin1.dat'
filename_sum = 'sum.dat'


def main():
    my_items = CashRegister()
    choice = 0
    sum = 0
    while choice != quit_:
        choice = get_menu_choice()
        if choice == show_:
            show_bin()
        elif choice == choose_:
            my_items,sum = item_input()
            save_items_to_bin(my_items)
            save_sum_to_bin(sum)
        elif choice == get_sum:
            sum = load_sum(filename_sum)
            print('Amount to pay: ',sum, "UAH")
        elif choice == clear_:
            clear()
            save_items_to_bin(my_items)
    save_items_to_bin(my_items)

if __name__ == '__main__':
   #main()

