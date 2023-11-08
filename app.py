from bank import Bank


class Game:

    @staticmethod
    def play_game(player_list, game_board):
        run_game = True
        turn_control = 0

        while run_game:
            current_player = player_list[turn_control]

            print('Tura gracza: ' + current_player.nick)
            input('Nacisnij Enter, aby rzucic kostka...')
            dice_roll = current_player.roll_dice()

            current_player.current_position = (current_player.current_position + dice_roll) % len(game_board)

            # current_field = game_board[current_player.current_position]

            print('Znajdujesz sie na polu: ' + game_board[current_player.current_position].name)

            interaction_result = game_board[current_player.current_position]

            if len(player_list) == 1:
                print('Gratulacje! Gracz ' + player_list[0].nick + ' zwyciezyl gre w monopoly!')
                run_game = False

            turn_control = (turn_control + 1) % len(player_list)
