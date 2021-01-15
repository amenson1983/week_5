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
from lesson_5_homework.answers import correct_answers_input, save_correct_answers, answers_input, save_user_answers
from lesson_5_homework.questions_class import get_menu_choice_questions, questions_input, save_questions

filename = 'correct_answers.dat'
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
            correct_answers = correct_answers_input()
            save_correct_answers(correct_answers)
            save_questions(questions)
        elif choice == start_:
            user_answers = answers_input()
            save_user_answers(user_answers)
        #elif choice == show_res:


        #elif choice == clear_:


if __name__ == '__main__':
   main()