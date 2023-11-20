from field import Field


class ActiveFields(Field):
    purchase = 0
    rents = []
    owner = None
    mortgage = 0
    mortgage_buyout = 0

    def __init__(self, identification, name, buyout, rent):
        super().__init__(identification, name)
        self.purchase = buyout
        self.rents = rent
        self.mortgage = int(self.purchase / 2)
        self.mortgage_buyout = self.mortgage + (self.mortgage * 0.1)


    def interact(self, player, player_list):
        super().interact(player, player_list)
