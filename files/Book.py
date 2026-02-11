from Gift import Gift

class Book(Gift):

    def description(self):
        self.gift_description = "A Book for you !"
        return self.gift_description