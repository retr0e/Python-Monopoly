from field import Field


class Start(Field):

    def __init__(self):
        super().__init__(0, 'START')

    def interact(self, player, player_list):
        player.money += 200
        input('Otrzymujesz 200 PLN. Nacisnij Enter aby kontynuowac...')

    @staticmethod
    def start_bonus(player):
        player.money += 200
