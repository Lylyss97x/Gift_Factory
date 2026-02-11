import random
import datetime
from Delivery_Context import Delivery_context
from Boat import Boat
from Truck import Truck
from Factory import Factory
from Custom import Custom

MAX_EMPLOYEE_PER_ORDER = 3

class Order:

    def __init__(self,customer_name, gift_type, custom, delivery_method):
        self.id = random.randint(0,100000)
        self.customer_name = customer_name
        self.gift_type = gift_type
        self.employee_busy_by = 0
        self.custom = custom
        self.delivery_method = delivery_method
        self.state = f"send at {datetime.datetime.now()} \n"
        self.order_description()
        self.notify_employee()
        self.trigger_order()
        self.delivered_order()

    def order_description(self):
        print(f'\nCommande ID : {self.id} \nName Customer {self.customer_name} \nGift Type : {self.gift_type} \nState : {self.state}')

    def trigger_order(self):
        gift = Factory().create_gift(self)
        Custom.decoration(self,gift)
        print(self.update_state("delivery occurred"))
        
    def delivered_order(self):
        print("")
        print(" ======== ORDER DELIVERY ! ========") 
        delivery_context = Delivery_context()
        print(delivery_context.trigger_delivery(self.delivery_method))
        print(self.update_state("finished"))
    
    def notify_employee(self):

        print("")
        print(" ======== EMPLOYEE NOTIFICATION ! ========")
        employee_factory = Factory().employees
        for i in range (len(employee_factory)):

            if self.employee_busy_by >= MAX_EMPLOYEE_PER_ORDER:
                print(f" The maximum number of employee is reached ")
                break

            elif not employee_factory[i].busy:
                employee_factory[i].busy = self.id
                self.employee_busy_by += 1
                print(f" Employee {employee_factory[i].number} : Notified for order {self.id} ")

            elif employee_factory[i].busy:
                print(f" Employee {employee_factory[i].number} is already busy with order {employee_factory[i].busy} ")

    def update_state(self,state):
       
       custom_state = Custom()

       if state == "finished":
           self.state += custom_state.finished_state() + f" at {datetime.datetime.now()} \n"

       elif state == "delivery occurred":
           self.state += custom_state.delivery_state() + f" at {datetime.datetime.now()} \n"

       return self.state
    
