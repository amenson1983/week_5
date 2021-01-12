class Pet:
    def __init__(self,name=None,type=None,age=None):
        self._name = name
        self._type = type
        self._age = age

    def input_name(self):
        self._name = input('Input name')

    def input_type(self):
        self._type = input('Input type')

    def input_age(self):
        self._age = input('Input age')

    def ret_name(self):
        return self._name

    def ret_type(self):
        return self._type

    def ret_age(self):
        return self._age

    def __str__(self):
        return "Name: " + self._name, "Type: " + self._type, "Age: " + self._age