from field import Field


class Start(Field):

    def __init__(self):
        super().__init__(0, 'START')

    def interact(self, player, player_list):
        super().interact()

    @staticmethod
    def get_start_bonus(player):
        player.money += 200

