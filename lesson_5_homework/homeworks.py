from lesson_5_homework.book_class import Book
from lesson_5_homework.car_class import car

#if __name__ == '__main__':
    #my_car = car()
    #my_car.show_ifmove()

if __name__ == '__main__':
   book1 = Book()
   book1.input_title()
   book1.input_author()
   book1.input_producer()
   print(book1.__str__())






