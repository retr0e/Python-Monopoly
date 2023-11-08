from active_fields import ActiveFields


class Railway(ActiveFields):

    def __init__(self, identification, name, buyout, rent):
        super().__init__(identification, name, buyout, rent)

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

            rent = self.rents[0 + Railway.calculate_railway_rent(player)]

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
    def calculate_railway_rent(player):
        multiplier = 0
        for proper in player.owned_properties:
            if isinstance(proper, Railway):
                multiplier += 1
        return multiplier

    @staticmethod
    def create_railways():
        railways = [Railway(5, 'DWORZEC ZACHODNI', 200, [25, 50, 100, 200]),
                    Railway(15, 'DWORZEC GDANSKI', 200, [25, 50, 100, 200]),
                    Railway(25, 'DWORZEC WSCHODNI', 200, [25, 50, 100, 200]),
                    Railway(35, 'DWORZEC CENTRALNY', 200, [25, 50, 100, 200])]

        return railways
