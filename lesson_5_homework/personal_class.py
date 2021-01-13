from lesson_5_homework.employee_class import Employee
import pickle

look_up_ = 1
add_ = 2
delete_ = 3
change_ = 4
quit_ = 5
filename = 'employees.dat'


def load_emploees():
    try:
        input_file = open(filename,'rb')
        my_emploees = pickle.load(input_file)
        input_file.close()
    except IOError:
        my_emploees = {}
    return my_emploees


def get_menu_choice():
    print('_____________________________')
    print('1. Look up')
    print('2. Add')
    print('3. Delete')
    print('4. Change')
    print('5. Quit')
    choice = int(input('Please make a choice: '))
    while choice < look_up_ or choice > quit_:
        choice = int(input('Please make a choice: '))
    return choice



def look_up(my_emploees):
        taxnum = str(input('Enter your tax number: '))
        message = my_emploees.get(taxnum)
        print(message)


def add_emp(my_emploees):
    taxnum = input('Put tax number:')
    name = input('Put name:')
    department = input('Put department:')
    position = input('Put position:')
    entry = Employee(taxnum, name, department,position)
    if taxnum not in my_emploees:
        my_emploees[taxnum] = entry
        print('Entry has been added')
    else: print('Entry already exists')


def delete_emp(my_emploees):
    taxnum = input("Input tax number for deletion: ")
    if taxnum in my_emploees:
        del my_emploees[taxnum]
    else: print('Tax number has not been found')


def change(my_emploees):
    taxnumber = input('Put tax number: ')
    if taxnumber in my_emploees:
        emploees1 = Employee()
        emploees1.input_taxnum()
        emploees1.input_name()
        emploees1.input_department()
        emploees1.input_position()
        name = emploees1.ret_name()
        taxnum = emploees1.ret_taxnum()
        department = emploees1.ret_department()
        position = emploees1.ret_position()
        entry = Employee(taxnum, name, department, position)
        my_emploees[taxnum] = entry
        print('Information has been updated')
    else: print('The number has not been found at dictionary')


def save_emploees(my_emploees):
    output_file = open(filename,'wb')
    pickle.dump(my_emploees, output_file)
    output_file.close()



def main():
    my_emploees = load_emploees()
    choice = 0
    while choice != quit_:
        choice = get_menu_choice()
        if choice == look_up_:
            look_up(my_emploees)
        elif choice == add_:
            add_emp(my_emploees)
        elif choice == delete_:
            delete_emp(my_emploees)
        elif choice == change_:
            change(my_emploees)
    save_emploees(my_emploees)


if __name__ == '__main__':
    main()
    #dict = load_emploees()
    #print(str(dict.get('304')))





