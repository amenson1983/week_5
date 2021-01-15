#Для создания этой программы напишите класс Question (Вопрос), который будет содержать
   # данные о вопросе викторины. Класс Question должен иметь атрибуты для приведенных
    #ниже данных:
    #• вопрос викторины;
    #• возможный ответ 1;
   # • возможный ответ 2;
    #• возможный ответ 3;
    #• возможный ответ 4;
   # • номер правильного ответа ( 1, 2, 3 или 4 ).
  #  Класс Question также должен иметь соответствующий метод
  #  получатели и методы-модификаторы.
   # init () , методы-
  #  Программа должна содержать список или словарь с 10 объектами Question, один для
  #  каждого вопроса викторины.
from lesson_5_homework.answers import correct_answers_input, save_correct_answers, answers_input, save_user_answers, \
    CorrectAnswers, load_user_answers, load_correct_answers
from lesson_5_homework.questions_class import get_menu_choice_questions, questions_input, save_questions, load_questions

filename = 'questions.dat'
filename1 = 'user_answers.dat'
filename0 = 'questions.dat'
create = 1
start_ = 2
show_res = 3
clear_ = 4
quit_ = 5


def main():
    choice = 0
    while choice != quit_:
        choice = get_menu_choice_questions()
        if choice == create:
            questions = questions_input()
            save_questions(questions)
        elif choice == start_:
            user_answers = answers_input()
            save_user_answers(user_answers)
        elif choice == show_res:
            user_answers = load_user_answers(filename1)
            correct_answers = load_correct_answers(filename0)
            count = 0
            for key in user_answers:
                    if correct_answers[key] == user_answers[key]:
                        count +=1
                    else: count +=0
            print(count)


        #elif choice == clear_:


if __name__ == '__main__':
    #user_answers = load_user_answers(filename1)
   # correct_answers = load_correct_answers(filename0)
    #print((user_answers))
   main()
   #questions = load_questions(filename)
   #for key in questions:
   #    print(key,questions[key])
   #correct_answers = correct_answers_input()
   #save_correct_answers(correct_answers)

    u