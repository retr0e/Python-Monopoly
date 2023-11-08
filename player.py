class Player:
    nick = 'default_name'
    money = 2000
    owned_properties = []
    current_position = 0

    def __init__(self, nick_name):
        self.nick = nick_name

    @staticmethod
    def create_players():
        players_amount = int(input('Ile osob będzie grac? (Max: 6)\n'))
        while players_amount < 2 or players_amount > 6:
            players_amount = int(input('Proszę wprowadz ilosc, ktora jest dopuszczalna\n(Min: 2)\n(Max: 6)\n'))

        players = []
        for i in range(0, players_amount):
            player_nickname = input('Jak bedzie nazywać się gracz P' + str(i + 1) + ': ')
            players.append(Player(player_nickname))

        return players

    def roll_dice(self):
        import random
        return random.randint(1, 6) + random.randint(1, 6)
