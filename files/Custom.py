import time

class Custom:
    
    def decoration(order, gift):

        print("")
        print(" ======== CREATION GIFT WITH DECORATION  ! ========") 

        if order.custom["msg"]:
            if not gift.gift_description:
                gift.gift_description = gift.description() + " With Love ♥ "
            else:
                gift.gift_description = gift.gift_description + " With Love ♥ "

        if order.custom["bear"]:
            if not gift.gift_description:
                gift.gift_description = gift.description() + " With Teddy Bear ʕ•ᴥ•ʔ "
            else:
                gift.gift_description = gift.gift_description + " With Teddy Bear ʕ•ᴥ•ʔ "

        print( gift.gift_description)
        time.sleep(5)

    def finished_state(self):
        return "finished"
    
    def delivery_state(self):
        return "delivery occured"