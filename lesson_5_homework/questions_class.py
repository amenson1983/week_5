import pickle

filename = 'questions.dat'


class Questions:
    def __init__(self, question=None, ans1=None, ans2=None,ans3=None,ans4=None, correct=None):
        self._question = question
        self._ans_1 = ans1
        self._ans_2 = ans2
        self._ans_3 = ans3
        self._ans_4 = ans4
        self._correct = correct

    def input_question(self):
        question = input('Input question: ')
        self._question = question

    def input_ans_1(self):
        ans_1 = input('Input answer 1: ')
        self._ans_1 = ans_1

    def input_ans_2(self):
        ans_2 = input('Input answer 2: ')
        self._ans_2 = ans_2

    def input_ans_3(self):
        ans_3 = input('Input answer 3: ')
        self._ans_3 = ans_3

    def input_ans_4(self):
        ans_4 = input('Input answer 4: ')
        self._ans_4 = ans_4

    def input_correct(self):
        correct = input('Input correct answer: ')
        self._correct = correct

    def ret_question(self):
        return self._question

    def ret_ans_1(self):
        return self._ans_1

    def ret_ans_2(self):
        return self._ans_2

    def ret_ans_3(self):
        return self._ans_3

    def ret_ans_4(self):
        return self._ans_4

    def ret_correct(self):
        return self._correct

    def __str__(self):
        return 'Variant 1: '+str(self.ret_ans_1())+'  Variant 2 : '+str(self.ret_ans_2())+'  Variant 3: '+str(self.ret_ans_3())+'  Variant 4 : '+str(self.ret_ans_4())

def load_questions(filename):
    try:
        input_file = open(filename, 'rb')
        questions = pickle.load(input_file)
        input_file.close()
    except IOError:
        questions = {}
    return questions




def save_questions(questions):
    output_file = open(filename,'wb')
    pickle.dump(questions, output_file)
    output_file.close()

def get_menu_choice_questions():
    print('_____________________________')
    print('1. Create questionary')
    print('2. Start victorine')
    print('3. Show results')
    print('4. Clear user results')
    print('5. Quit')
    choice = int(input('Please make a choice: '))
    while choice < 1 or choice > 5:
        choice = int(input('Please make a choice: '))
    return choice

def questions_input():
   questions1 = Questions()
   questions = {}
   for person_num in range(0, 10):
      questions1.input_question()
      questions1.input_ans_1()
      questions1.input_ans_2()
      questions1.input_ans_3()
      questions1.input_ans_4()

      question = questions1.ret_question()
      answer_1 = questions1.ret_ans_1()
      answer_2 = questions1.ret_ans_2()
      answer_3 = questions1.ret_ans_3()
      answer_4 = questions1.ret_ans_4()

      items = Questions(question, answer_1, answer_2,answer_3,answer_4)
      questions[question] = items
      print(questions)
   return questions


