from field import Field


class Tax(Field):
    money_hit = 0

    def __init__(self, identification, name, money_hit):
        super().__init__(identification, name)
        self.money_hit = money_hit

    @staticmethod
    def create_taxes_field():
        Tax(4, 'PODATEK DOCHODOWY', 200)
        Tax(38, 'DOMIAR PODATKOWY', 100)