class Car_task:
    def __init__(self, speed=0, make=None, yearmodel=None):
        self._speed = speed
        self._make = make
        self._yearmodel = yearmodel


    def input_make(self,_make):
        self._make = _make

    def input_yearmodel(self,yearmodel):
        self._yearmodel = yearmodel

    def ret_speed(self):
        return self._speed

    def ret_make(self):
        return self._make

    def ret_yearmodel(self):
        return self._yearmodel

    def start(self):
        self._speed+=25

    def accelerate(self):
        self._speed+=5

    def brake(self):
        self._speed-=5

    def __str__(self):
        return "CURRENT SPEED IS: " + str(self._speed) + " kmph"