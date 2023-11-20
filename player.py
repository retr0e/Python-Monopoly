from bank import Bank

class Player:
    id = 0
    nick = 'default_name'
    money = 2000
    owned_properties = []
    current_position = 0

    def __init__(self, identi, nick_name):
        self.id = identi
        self.nick = nick_name

    @staticmethod
    def create_players():
        players_amount = int(input('Ile osob będzie grac? (Max: 6)\n'))
        while players_amount < 2 or players_amount > 6:
            players_amount = int(input('Proszę wprowadz ilosc, ktora jest dopuszczalna\n(Min: 2)\n(Max: 6)\n'))

        players = []
        for i in range(0, players_amount):
            player_nickname = input('Jak bedzie nazywać się gracz P' + str(i + 1) + ': ')
            players.append(Player(i, player_nickname))

        return players

    def roll_dice(self):
        import random
        return random.randint(1, 6) + random.randint(1, 6)

    def make_a_deal(self, player_list):
        print('Wybierz z kim chcesz handlowac:')
        decision_control_id = []
        for player in player_list:
            print(str(player.id) + ' - ' + player.nick)
            decision_control_id.append(player.id)

        pick_check = False
        customer_pick = -1
        # Sprawdzenie czy id gracza jest mozliwe do operacji
        while not pick_check:
            customer_pick = int(input('Decyzja: '))
            for x in decision_control_id:
                if x == customer_pick:
                    pick_check = True

            if not pick_check:
                print('Nie podałeś właściwego gracza!')

        if customer_pick != -1 and pick_check:
            Bank.trade_properties(self, player_list[customer_pick])

