from Order import Order
from Boat import Boat
from Truck import Truck


class Interface:

    MAX_ATTEMPT = 3

    def main():
        while True:
            print("###################################")
            print("#                                 #")
            print("# ~~~~~~~~  GIFT FACTORY ~~~~~~~~ #")
            print("#                                 #")
            print("###################################")
            choice = input("- Take an order press key '1' \n- Other Key will Exit the program \n")
            if choice == "1":
                Interface.menu()
            else:
                print("End of the program. Thank You !")
                break


    def menu():
        attempt = 0
        while attempt < Interface.MAX_ATTEMPT:
            print("")
            print(" ======== PURCHASE ORDER ========")
            name = input("Enter a name for the order \n")
            name = Interface.input_name(name)

            gift_type = input("Enter the number of the gift you want to send \n 1. Toy \n 2. Book \n 3. Video Game \n")
            gift_type =Interface.input_gift_type(gift_type)
            while not gift_type and attempt < Interface.MAX_ATTEMPT:
                attempt += 1
                print("#### Error : Enter 1, 2 or 3 \n")
                gift_type = input("Enter the number of the gift you want to send \n 1. Toy \n 2. Book \n 3. Video Game \n")
                gift_type =Interface.input_gift_type(gift_type)
            if not gift_type or attempt >= Interface.MAX_ATTEMPT:
                print("#### Too much Value Invalid, Relaunch program")
                break

            msg = input("Do you want a love message with the gift ? yes/no \n")
            choice_msg = Interface.input_msg(msg)
            while not choice_msg and attempt < Interface.MAX_ATTEMPT:
                attempt += 1
                print("#### Error : Enter yes or no \n")
                msg = input("Do you want a love message with the gift ? yes/no \n")
                choice_msg =Interface.input_msg(msg)
            if not choice_msg or attempt >= Interface.MAX_ATTEMPT:
                print("#### Too much Value Invalid, Relaunch program")
                break

            bear = input("Do you want a teddy bear with the gift ? yes/no \n")
            choice_msg_bear = Interface.input_bear(bear,choice_msg)
            while not choice_msg_bear and attempt < Interface.MAX_ATTEMPT:
                attempt += 1
                print("#### Error : Enter yes or no \n")
                bear = input("Do you want a teddy bear with the gift ? yes/no \n")
                choice_msg_bear =Interface.input_bear(bear,choice_msg)
            if not choice_msg_bear or attempt >= Interface.MAX_ATTEMPT:
                print("#### Too much Value Invalid, Relaunch program")
                break

            delivery_method = input("Choose your method of delivery ? boat/truck \n")
            delivery_method = Interface.input_method_delivery(delivery_method)
            while not delivery_method and attempt < Interface.MAX_ATTEMPT:
                attempt += 1
                print("#### Error : Enter boat or truck \n")
                delivery_method = input("Choose your method of delivery ? boat/truck \n")
                delivery_method =Interface.input_method_delivery(delivery_method)
            if not delivery_method or attempt >= Interface.MAX_ATTEMPT:
                print("#### Too much Value Invalid, Relaunch program")
                break
            print("")
            print(" ======== ORDER SEND ! ========")
            Order(name,gift_type,choice_msg_bear,delivery_method)
            break


    def input_name(input):
        try:
            name = str(input)
        except ValueError as e:
            print("Invalid value error")

        return name
    
    def input_gift_type(input):
        try:
            gift_type = int(input)
        except ValueError as e:
            return 0

        if gift_type == 1:
            return "toy"
        
        elif gift_type == 2:
            return "book"
        
        elif gift_type == 3:
            return "video_game"
        else:
            return 0
        
    def input_msg(input):
        
        custom_msg = {}
        
        if input == "yes":
            custom_msg["msg"] = True
            return custom_msg
        
        elif input =="no":
            custom_msg["msg"] = False
            return custom_msg
        else:
            return 0
        
    def input_bear(input, custom):
        
        if input == "yes":
            custom["bear"] = True
            return custom
        
        elif input =="no":
            custom["bear"] = False
            return custom
        else:
            return 0
        
    def input_method_delivery(input):
        
        if input == "boat":
            return Boat()
        
        elif input =="truck":
            return Truck()
        else:
            return 0

             
Interface.main()


    


