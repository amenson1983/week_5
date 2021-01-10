import random
class car:
    def __init__(self):
        self.go = 0


    def show_ifmove(self):
        go = random.randint(0,1)
        if go == 0:
            print('Car goes')
        else: print('Car is stopped')



