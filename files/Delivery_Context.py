import time

class Delivery_context:

    def trigger_delivery(self,method_delivery):

        for i in range(0,20):
            delivery_status = ["."]*20
            delivery_status[i] = method_delivery.symbol
            print(" ".join(delivery_status),end="\r")
            time.sleep(0.1)

        return method_delivery.send()