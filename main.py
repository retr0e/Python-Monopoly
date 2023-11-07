# ------------ IMPORTS ------------

from active_fields import ActiveFields
from field import Field
from parking import Parking
from player import Player
from property import Property
from start import Start
from tax import Tax
from utility import Utility
from bank import Bank

# ------------ FUNCTIONS ------------


def show_menu():

    print('WITAJ W MONOPOLY!')
    print('1 - Rozpocznij rozgrywke')
    print('2 - Wczytaj poprzednią rozgrywke')
    print('3 - Zasady obecnej wersji gry')
    print('4 - Nie mam czasu na to! Wyjdz.')


# ------------ MAIN PROGRAM ------------

show_menu()
play_monopoly = True

while play_monopoly:
    print(Player.create_players())

    play_monopoly = False
