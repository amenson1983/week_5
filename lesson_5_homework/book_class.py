import pickle
class Book:
    def __init__(self,title=None,author=None,producer=None):
        self.title = title
        self.author = author
        self.producer = producer

    def input_title(self):
        self.title = input('Input title')

    def input_author(self):
        self.author = input('Input author')

    def input_producer(self):
        self.producer = input('Input producer')

    def ret_title(self):
        return self.title

    def ret_author(self):
        return self.author

    def ret_producer(self):
        return self.producer



    def __str__(self):
        return "Title: " + self.title, "Author: " + self.author, "Producer: " + self.producer




