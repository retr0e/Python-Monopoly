from field import Field


class ActiveFields(Field):
    purchase = 0
    rents = []
    owner = None
    mortgage = 0
    mortgage_buyout = 0

    def __init__(self, identification, name, property_cost, rent, mortgage, mortgage_to_pay):
        self.id = identification
        self.name = name
        self.purchase = property_cost
        self.rents = rent
        self.mortgage = mortgage
        self.mortgage_buyout = mortgage_to_pay
        