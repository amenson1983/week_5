from lesson_5_homework.answers import Answers
from lesson_5_homework.questions_class import Questions, get_menu_choice_questions
import pickle

filename = 'questions.dat'
filename1 = 'user_answers.dat'
filename0 = 'correct_answers.dat'
create = 1
start_ = 2
show_res = 3
clear_ = 4
quit_ = 5
question_list = {}
correct_list = {}
user_list = {}

def questions_input1():
    for i in range(0,2):
        first_question = Questions()
        first_question.input_question()
        first_question.input_ans_1()
        first_question.input_ans_2()
        first_question.input_ans_3()
        first_question.input_ans_4()
        first_question.input_correct()
        question = first_question.ret_question()
        correct_answer = first_question.ret_correct()
        var1 = first_question.ret_ans_1()
        var2 = first_question.ret_ans_2()
        var3 = first_question.ret_ans_3()
        var4 = first_question.ret_ans_4()
        message1 = str('   Variant 1 : ' + var1 +'   Variant 2 : ' + var2)
        message2 = str('   Variant 3 : ' + var3 +'   Variant 4 : ' + var4)
        message = message1 + message2
        question_list[question] = message
        correct_item = correct_answer
        correct_list[question] = correct_item
        save_questions1(question_list)
        save_correct_answers1(correct_list)
    return question_list,correct_list

def save_questions1(question_list):
    output_file = open(filename,'wb')
    pickle.dump(question_list, output_file)
    output_file.close()

def load_questions1(filename):
    try:
        input_file = open(filename, 'rb')
        question_list = pickle.load(input_file)
        input_file.close()
    except IOError:
        question_list = {}
    return question_list

def save_correct_answers1(correct_list):
    output_file = open(filename0, 'wb')
    pickle.dump(correct_list, output_file)
    output_file.close()

def load_correct_answers1(filename0):
    try:
        input_file = open(filename0, 'rb')
        correct_answers = pickle.load(input_file)
        input_file.close()
    except IOError:
        correct_answers = {}
    return correct_answers

def save_user_answers1(user_list):
    output_file = open(filename1, 'wb')
    pickle.dump(user_list, output_file)
    output_file.close()

def load_user_answers1(filename1):
    try:
        input_file = open(filename1, 'rb')
        user_list = pickle.load(input_file)
        input_file.close()
    except IOError:
        user_list = {}
    return user_list

def victorine(question_list):
    user_list = {}
    first_answer = Answers()
    for question in question_list:
        print(question, "\n", question_list[question])
        first_answer.input_user_answer()
        answer = first_answer.ret_user_answer()
        user_list[question] = answer
    return user_list

def main():
    choice = 0
    while choice != quit_:
        choice = get_menu_choice_questions()
        if choice == create:
            question_list, correct_list = questions_input1()
            save_questions1(question_list)
            save_correct_answers1(correct_list)
        elif choice == start_:
            question_list = load_questions1(filename)
            user_list = victorine(question_list)
            save_user_answers1(user_list)
        elif choice == show_res:
            user_list = load_user_answers1(filename1)
            correct_answers = load_correct_answers1(filename0)
            sum = 0
            for key in user_list:
                if user_list[key] == correct_answers[key]:
                    sum +=1
            print('Total score: ', sum)
        elif choice == clear_:
            user_list = load_user_answers1(filename1)
            user_list.clear()
            save_user_answers1(user_list)

if __name__ == '__main__':
    main()
    #user_list = load_questions1(filename)
    #correct_list = load_correct_answers1(filename0)





