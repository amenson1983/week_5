class Employee:
    def __init__(self, taxnum = None, name = None, department=None,position=None):
        self._name = name
        self._taxnum = taxnum
        self._department = department
        self._position = position

    def show(self):
        print(self._name, self._taxnum, self._department, self._position)

    def input_name(self):
        name = input('Input name: ')
        self._name = name

    def input_taxnum(self):
        taxnum = input('Input taxnum: ')
        self._taxnum = taxnum

    def input_department(self):
        department = input('Input department: ')
        self._department = department

    def input_position(self):
        position = input('Input position: ')
        self._position = position

    def ret_name(self):
        return self._name

    def ret_taxnum(self):
        return self._taxnum

    def ret_department(self):
        return self._department

    def ret_position(self):
        return self._position


    def get_from_file(self, filename):
        with open(filename, "r", encoding="UTF") as myfile:
            user_str = myfile.readline()
        user = tuple(user_str.split(";"))
        self._name = user[0]
        self._taxnum = user[1]
        self._department = user[2]
        self._position = user[3]

    def save_to_file(self, filename):
        with open(filename, "w", encoding="UTF") as myfile:
            user = []
        user[0] = self._name
        user[1] = self._taxnum
        user[2] = self._department
        user[3] = self._position

    def __str__(self):
        return "Name : " + str(self._name) + "\n" + "Taxnum : " + str(self._taxnum) + "\n" + "Department : " + str(self._department) + "\nPosition : " + str(self._position)
