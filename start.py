from field import Field


class Start(Field):
    @staticmethod
    def get_start_bonus(player):
        player.money += 200
