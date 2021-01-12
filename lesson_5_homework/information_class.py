class Information:
    def __init__(self, name=None, adress=None, age=None,phone=None):
        self._name = name
        self._adress = adress
        self._age = age
        self._phone = phone

    def input_name(self):
        name = input('Input name: ')
        self._name = name

    def input_adress(self):
        adress = input('Input adress: ')
        self._adress = adress

    def input_age(self):
        age = input('Input age: ')
        self._age = age

    def input_phone(self):
        phone = input('Input phone: ')
        self._phone = phone

    def ret_name(self):
        return self._name

    def ret_adress(self):
        return self._adress

    def ret_age(self):
        return self._age

    def ret_phone(self):
        return self._phone

    def __str__(self):
        return "Name : " + self._name + "\n" + "Age : " + str(self._age) + "\n" + "Adress : " + self._adress + "\nPhone : " + str(self._phone)


def person_input_for_3():
   person_me = Information()
   list_persons = []
   for person_num in range(0, 3):
      person_me.input_name()
      person_me.input_age()
      person_me.input_adress()
      person_me.input_phone()
      name = person_me.ret_name()
      age = person_me.ret_age()
      adress = person_me.ret_adress()
      phone = person_me.ret_phone()
      person = Information(name,age,adress,phone)
      list_persons.append(person)
   return list_persons


def person_display_for_3(list_persons):
   for person in list_persons:
      print(person.ret_name())
      print(person.ret_age())
      print(person.ret_adress())
      print(person.ret_phone())
      print()
