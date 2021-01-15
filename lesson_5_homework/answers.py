import pickle



filename = 'questions.dat'
filename1 = 'user_answers.dat'
filename0 = 'correct_answers.dat'

class Answers:
    def __init__(self, question=None, user_answer=None):
        self._question = question
        self._user_answer = user_answer

    def input_user_answer(self):
        user_answer = input('Input answer please: ')
        self._user_answer = user_answer

    def ret_user_answer(self):
        return self._user_answer



class CorrectAnswers:
    def __init__(self, question=None, correct_answer=None):
        self._question = question
        self._correct_answer = correct_answer

    def input_user_answer(self):
        correct_answer = input('Set correct answer please: ')
        self._correct_answer = correct_answer

    def ret_correct_answer(self):
        return self._correct_answer



def answers_input():
    answers1 = Answers()
    questions = load_questions(filename)
    answers = {}
    for key in questions:
        print(key)
        print(questions[key])
        answers1.input_user_answer()
        user_answer = answers1.ret_user_answer()
        items = Answers(key, user_answer)
        answers[key] = items
        print(answers)
    return answers


def load_user_answers(filename1):
    try:
        input_file = open(filename1, 'rb')
        user_answers = pickle.load(input_file)
        input_file.close()
    except IOError:
        user_answers = {}
    return user_answers




def save_user_answers(user_answers):
    output_file = open(filename1, 'wb')
    pickle.dump(user_answers, output_file)
    output_file.close()






def correct_answers_input():
    correct_answers1 = Answers()
    questions = load_questions(filename)
    correct_answers = {}
    for question in questions:
        print(question)
        correct_answers1.input_user_answer()
        user_answer = correct_answers1.ret_user_answer()
        items = Answers(question, user_answer)
        correct_answers[question] = items
        print(correct_answers)
    return correct_answers

def save_correct_answers(correct_answers):
    output_file = open(filename0, 'wb')
    pickle.dump(correct_answers, output_file)
    output_file.close()

def load_correct_answers(filename0):
    try:
        input_file = open(filename0, 'rb')
        correct_answers = pickle.load(input_file)
        input_file.close()
    except IOError:
        correct_answers = {}
    return correct_answers

def load_questions(filename):
    try:
        input_file = open(filename, 'rb')
        questions = pickle.load(input_file)
        input_file.close()
    except IOError:
        questions = {}
    return questions
#def show_results():
