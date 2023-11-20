from active_fields import ActiveFields


class Property(ActiveFields):
    def __init__(self, identification, name, buyout, rent, house_price):
        super().__init__(identification, name, buyout, rent)
        self.available_hotel = False
        self.houses = 0
        self.house_price = house_price
        self.hotel_price = house_price * 5
        self.active = True

    def interact(self, player, player_list):
        # Pole nie nalezy do nikogo
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

        # Pole jest zakupione
        else:

            rent = self.calculate_rent()
            # Gracz jest wlascicielem
            if player == self.owner:
                # Kupowanie domkow/hotelu
                print('1 - Kup domek/hotel')
                print('2 - Nie rob nic')

                decision = int(input('Decyzja: '))
                while decision < 1 or decision > 2:
                    decision = int(input('Decyzja: '))

                match decision:
                    case 1:
                        if self.houses < 4:
                            if player.money >= self.house_price:
                                player.money -= self.house_price
                                self.houses += 1
                                print('Kupiles wlasnie domek dla pola ' + self.name)
                            else:
                                print('Nie masz wystarczajaco pieniedzy do kupienia domku')
                        elif self.houses == 4:
                            if player.money >= self.hotel_price:
                                player.money -= self.hotel_price
                                self.houses += 1
                                print('Zakupiles hotel dla pola ' + self.name)
                            else:
                                print('Nie stac Cie na hotel!')
                    case 2:
                        return

            # Gracz nie jest wlasicielem
            else:
                print('Gracz ' + player.nick + 'znalazl sie na polu ' + self.name +
                      ' ktore nalezy do ' + self.owner.nick + '.')
                print('Musisz zaplacic ' + str(rent) + ' PLN czynszu graczowi -> ' + self.owner.nick)

                if player.money >= rent:
                    player.money -= rent
                    self.owner.money += rent
                else:
                    # Bankructwo gracza
                    print('Gracz ' + player.nick + ' nie posiada wystarczajaco pieniedzy.\n')
                    print('Nie jestes w stanie sie utrzymac wiec czeka Cie BANKRUCTWO!')
                    player_list.remove(player)

    def calculate_rent(self):
        return self.rents[self.houses]

    @staticmethod
    def show_properties(player):
        for land in player.owned_properties:
            print(land.name)

    @staticmethod
    def create_properties():
        properties = [
            Property(1, 'ULICA KONOPACKA', 60, [4, 10, 30, 90, 160, 250], 50),
            Property(3, 'ULICA STALOWA', 60, [8, 20, 60, 180, 320, 450], 50),
            Property(6, 'ULICA RADZYMINSKA', 100, [12, 30, 90, 270, 400, 550], 50),
            Property(8, 'ULICA JAGIELONSKA', 100, [12, 30, 90, 270, 400, 550], 50),
            Property(9, 'ULICA TARGOWA', 120, [16, 40, 100, 300, 450, 600], 50),
            Property(11, 'ULICA PLOWIECKA', 140, [20, 50, 150, 450, 625, 750], 100),
            Property(13, 'ULICA MARSA', 140, [20, 50, 150, 450, 625, 750], 100),
            Property(14, 'ULICA GROCHOWSKA', 160, [24, 60, 180, 500, 700, 900], 100),
            Property(16, 'ULICA OBOZOWA', 180, [28, 70, 200, 550, 750, 950], 100),
            Property(18, 'ULICA GORCZEWSKA', 180, [28, 70, 200, 550, 750, 950], 100),
            Property(19, 'ULICA WOLSKA', 200, [32, 80, 220, 600, 800, 1000], 100),
            Property(21, 'ULICA MICKIEWICZA', 220, [36, 90, 250, 700, 875, 1050], 150),
            Property(23, 'ULICA SLOWACKIEGO', 220, [36, 90, 250, 700, 875, 1050], 150),
            Property(24, 'PLAC WILSONA', 240, [40, 100, 300, 750, 925, 1100], 150),
            Property(26, 'ULICA SWIETOKRZYSKA', 260, [44, 110, 330, 800, 975, 1150], 150),
            Property(27, 'KRAKOWSKIE PRZEDMIESCIE', 260, [44, 110, 330, 800, 975, 1150], 150),
            Property(29, 'NOWY SWIAT', 280, [48, 120, 360, 850, 1025, 1200], 150),
            Property(31, 'PLAC TRZECH KRZYZY', 300, [52, 130, 390, 900, 1100, 1275], 200),
            Property(32, 'ULICA MARSZALKOWSKA', 300, [52, 130, 390, 900, 1100, 1275], 200),
            Property(34, 'ALEJE JEROZOLIMSKIE', 320, [56, 150, 450, 1000, 1200, 1400], 200),
            Property(37, 'ULICA BELWEDERSKA', 350, [70, 175, 500, 1100, 1300, 1500], 200),
            Property(39, 'ALEJE UJAZDOWSKIE', 400, [100, 200, 600, 1400, 1700, 2000], 200)
        ]

        return properties
