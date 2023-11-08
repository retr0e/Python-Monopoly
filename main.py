# ------------ IMPORTS ------------

from active_fields import ActiveFields
from field import Field
from parking import Parking
from start import Start
from player import Player
from property import Property
from tax import Tax
from utility import Utility
from railway import Railway
from app import Game
from bank import Bank


def create_game_grid():
    board = (Property.create_properties() + Utility.create_utilities() + Railway.create_railways()
             + Tax.create_taxes_field() + Field.create_fields())
    board.append(Start())
    board.append(Parking())

    # Bubble sort to organize grid
    for i in range(0, len(board)):
        no_change = True
        for j in range(0, len(board) - i - 1):
            if board[j].id > board[j + 1].id:
                no_change = False
                temp = board[j]
                board[j] = board[j + 1]
                board[j + 1] = temp
        if no_change:
            break

    return board


def show_menu():
    print('WITAJ W MONOPOLY!')
    print('1 - Rozpocznij rozgrywke')
    print('2 - Wczytaj poprzednią rozgrywke')
    print('3 - Zasady obecnej wersji gry')
    print('4 - Nie mam czasu na to! Wyjdz.')


def rules():
    print('ZASADY:')
    print('Napisze je kiedys')

# ------------ MAIN PROGRAM ------------


show_menu()
decision = int(input('Wybierz akcje: '))

while decision < 1 or decision > 4:
    decision = int(input('Podaj prawidłową opcje'))

match decision:
    case 1:
        Game.play_game(Player.create_players(), create_game_grid())
    case 2:
        print('Wczytywanie')
    case 3:
        rules()
    case 4:
        print('Bye bye!')
        