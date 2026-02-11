from Gift import Gift

class Toy(Gift):

    def description(self):
        self.gift_description = "A Toy for you !"
        return self.gift_description
