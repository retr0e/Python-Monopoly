import pickle
from bank import Bank
from start import Start


def save_game_state(player_list, game_board):
    game_state = {'players': player_list, 'board': game_board}
    with open('monopoly_game_state.pkl', 'wb') as file:
        pickle.dump(game_state, file)
    # print('Game saved')


class Game:

    @staticmethod
    def play_game(player_list, game_board):
        run_game = True
        turn_control = 0

        while run_game:
            current_player = player_list[turn_control]

            print('Tura gracza: ' + current_player.nick + ' twoje fundusze: ' + str(current_player.money))

            input('Nacisnij Enter, aby rzucic kostka...')
            dice_roll = current_player.roll_dice()

            if current_player.current_position + dice_roll > 40:
                current_player.money += Start.start_bonus(current_player)

            current_player.current_position = (current_player.current_position + dice_roll) % len(game_board)

            print('Znajdujesz sie na polu: ' + game_board[current_player.current_position].name)

            game_board[current_player.current_position].interact(current_player, player_list)

            if len(player_list) == 1:
                print('Gratulacje! Gracz ' + player_list[0].nick + ' zwyciezyl gre w monopoly!')
                run_game = False

            print(' ')
            save_game_state(player_list, game_board)
            turn_control = (turn_control + 1) % len(player_list)
