class Patient:
    def __init__(self, fio=None, adress=None, emergphone=None, phone=None):
        self._fio = fio
        self._adress = adress
        self._emergphone = emergphone
        self._phone = phone

    def input_fio(self):
        fio = input('Input name: ')
        self._fio = fio

    def input_adress(self):
        adress = input('Input adress: ')
        self._adress = adress

    def input_emergphone(self):
        emergphone = input('Input emergency phone: ')
        self._emergphone = emergphone

    def input_phone(self):
        phone = input('Input your phone: ')
        self._phone = phone

    def ret_fio(self):
        return self._fio

    def ret_adress(self):
        return self._adress

    def ret_emergphone(self):
        return self._emergphone

    def ret_phone(self):
        return self._phone

    def __str__(self):
        return "FIO : " + str(self.ret_fio()) + "\n" + "emergphone : " + str(self.ret_emergphone()) + "\n" + "Adress : " + str(self.ret_adress()) + "\nPhone : " + str(self.ret_phone())


def person_input_for_1():
    person_me = Patient()
    list_persons = []
    for person_num in range(0, 1):
        person_me.input_fio()
        person_me.input_emergphone()
        person_me.input_adress()
        person_me.input_phone()
        fio = person_me.ret_fio()
        emergphone = person_me.ret_emergphone()
        adress = person_me.ret_adress()
        phone = person_me.ret_phone()
        person = Patient(fio, emergphone, adress, phone)
        list_persons.append(person)
    return list_persons


def person_display(list_persons):
    for person in list_persons:
        print(person.ret_fio())
        print(person.ret_emergphone())
        print(person.ret_adress())
        print(person.ret_phone())
        print()
