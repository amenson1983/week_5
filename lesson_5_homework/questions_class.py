class Questions:
    def __init__(self, question=None, correct_answer=None, ans1=None):
        self._question = question
        self._correct_answer = correct_answer
        self._ans_1 = ans1


    def input_question(self):
        question = input('Input question: ')
        self._question = question

    def input_correct_answer(self):
        correct_answer = input('Input correct_answer: ')
        self._correct_answer = correct_answer

    def input_price(self):
        ans_1 = input('Input ans1: ')
        self._ans_1 = ans_1


    def ret_question(self):
        return self._question

    def ret_correct_answer(self):
        return self._correct_answer

    def ret_ans_1(self):
        return self._ans_1

    def get_sum_(self):
        price = self.ret_ans_1
        quantity = self.ret_correct_answer()
        sum = float(price) * float(quantity)
        return sum