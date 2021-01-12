from lesson_5_homework.book_class import Book
from lesson_5_homework.car_class import car

#if __name__ == '__main__':
    #my_car = car()
    #my_car.show_ifmove()

#if __name__ == '__main__':
   #book1 = Book()
   #book1.input_title()
   #book1.input_author()
   #book1.input_producer()
   #print(book1.__str__())
from lesson_5_homework.car_class_task import Car_task
from lesson_5_homework.employee_class import Employee, employee_to_list, employee_display_for_3, \
   data_employee_input_to_file
from lesson_5_homework.information_class import Information, person_input_for_3, person_display_for_3
from lesson_5_homework.pet_class import Pet

#if __name__ == '__main__':
   #pet1 = Pet()
   #pet1.input_name()
   #pet1.input_type()
   #pet1.input_age()
   #name = pet1.ret_name()
   #type = pet1.ret_type()
   #age = pet1.ret_age()
   #print(pet1.__str__(), '\n',name, '\n',type,
   #      '\n',age)

#if __name__ == '__main__':
   #car = Car_task()
   #manufacturer = car.input_make('Renault')
   #year = car.input_yearmodel('2015')
   #car.start()
   #speed = car.ret_speed()
   #for i in range(0,6):
      #car.accelerate()
      #print(car.__str__())
   #for i in range(0,6):
      #car.brake()
      #print(car.__str__())
   #speed = car.ret_speed()


from lesson_5_homework.information_class import Information
#if __name__ == '__main__':
   #list = person_input_for_3()
   #person_display_for_3(list)
   #print(list)



#if __name__ == '__main__':
   #employee = Employee()
   #list_persons = person_input_for_3()
   #person_display_for_3(list_persons)


  # print(list_persons)
from lesson_5_homework.realitem_class import Realitem, item_input_for_3, item_display_for_3

if __name__ == '__main__':
   realitem = Realitem()
   list_items = item_input_for_3()
   item_display_for_3(list_items)