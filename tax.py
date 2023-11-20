from field import Field


class Tax(Field):
    # money_hit = 0

    def __init__(self, identification, name):
        super().__init__(identification, name)
        # self.money_hit = money_hit

    def interact(self, player, player_list):
        # player.money -= self.money_hit
        value_of_properties = int(input('Jaka jest wartosc twoich nieruchomosci?'))
        money_hit = value_of_properties * 0.01
        print('Zabolalo cie wlasnie: ', str(money_hit))
        player.money -= money_hit

    @staticmethod
    def create_taxes_field():
        taxes = [Tax(4, 'PODATEK DOCHODOWY'),
                 Tax(38, 'DOMIAR PODATKOWY')]

        return taxes
