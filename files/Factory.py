import time
from Toy import Toy
from Book import Book
from Video_Game import Video_game
from Employee import Employee

MAX_EMPLOYEE = 10

class Factory:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.gifts = []
            cls._instance.employees = []
            cls._instance.create_employee()
        return cls._instance
    
    def create_employee(self):

        for i in range (0,MAX_EMPLOYEE):
            self.employees.append(Employee())
            
    def create_gift(self, order):

        gift = None
    
        if order.gift_type == "toy":
            gift = Toy()
        
        elif order.gift_type == "book":
            gift = Book()

        elif order.gift_type == "video_game":
            gift = Video_game()

        else:
            gift = "Unknow type"

        self.gifts.append(gift)
        time.sleep(2)
        return gift