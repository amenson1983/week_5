from lesson_5_homework.patient_class import Patient


class Procedure:
    def __init__(self, proced_name=None, proced_date=None, proced_doctor_name=None, proced_cost=None):
        self._proced_name = proced_name
        self._proced_date = proced_date
        self._proced_doctor_name = proced_doctor_name
        self._proced_cost = proced_cost

    def set_proced_name(self):
        self._proced_name = input('Input procedure name:')

    def set_proced_date(self):
        self._proced_date = input('Input procedure_date: ')

    def set_proced_doctor_name(self):
        self._proced_doctor_name = input('Input doctor name: ')

    def set_proced_cost(self):
        self._proced_cost = input('Input cost: ')

    def ret_proced_name(self):
        return self._proced_name

    def ret_proced_date(self):
        return self._proced_date

    def ret_doctor_name(self):
        return self._proced_doctor_name

    def ret_cost(self):
        return self._proced_cost

    def __str__(self):
        return "FIO : " + str(self.ret_proced_name()) + "\n" + "emergphone : " + str(self.ret_proced_date()) + "\n" + "Adress : " + str(self.ret_doctor_name()) + "\nPhone : " + str(self.ret_cost())



