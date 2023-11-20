from active_fields import ActiveFields


class Utility(ActiveFields):
    bonus = 0

    def __init__(self, identification, name, buyout):
        super().__init__(identification, name, buyout, 0)
        self.bonus = 4
        self.active = True

    def interact(self, player, player_list):
        if self.owner is None:

            purchase_decision = input('Czy chcesz kupic: ' + self.name + ' za ' +
                                      str(self.purchase) + ' PLN? (Y/N): ').lower()

            if purchase_decision == 'y':
                if player.money >= self.purchase:
                    player.money -= self.purchase
                    self.owner = player
                    player.owned_properties.append(self)
                    print('Zakupiles/as: ' + self.name)
                else:
                    print('Nie masz pieniedzy do zakupu tego pola: ' + self.name)
            else:
                print('Gracz odrzuca oferte kupna pola: ' + self.name)

        else:

            if self.owner == player:
                print('To twoje pole. Nic sie na nim nie da juz zrobic')
                return

            input('Rzuc koscia aby wyliczyc koszty. Nacisnij Enter...')

            rent = player.roll_dice() * self.bonus
            print('Gracz ' + player.nick + 'znalazl sie na polu ' + self.name +
                  ' ktore nalezy do ' + self.owner.nick + '.')
            print('Musisz zaplacic ' + str(rent) + ' PLN graczowi -> ' + self.owner.nick)

            if player.money >= rent:
                player.money -= rent
                self.owner.money += rent
            else:
                # Bankructwo gracza
                print('Gracz ' + player.nick + ' nie posiada wystarczajaco pieniedzy.\n')
                print('Nie jestes w stanie sie utrzymac wiec czeka Cie BANKRUCTWO!')
                player_list.remove(player)

    @staticmethod
    def create_utilities():
        utilities = [Utility(12, 'ELEKTROWNIA', 150),
                     Utility(28, 'WODOCIAGI', 150)]

        return utilities
