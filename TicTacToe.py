def game_start():
    invalid = True
    while invalid == True:
        player_choice = input("Welcome to the TicTacToe game! What would you like to play as? X or O? ")
        if player_choice.upper() not in ['X','O']:
            print("That is not a valid input!")
        elif player_choice.upper() in ['X', 'O']:
            print("That is a valid input!")
            invalid = False
    print("The player with the X starts!\n")   

def replay():
    willingness = False
    while willingness == False:
        replay_input = input("Replay? Y / N ?")
        if replay_input.upper() not in ['Y','N']:
            print("Please press Y or N.")
        elif replay_input.upper() == 'Y':
            willingness = True
            return True
        else:
            willingness = True
            return False
            
def game():
    board_row_1 = [' ', 7, '|', 8, '|', 9, ' ']
    board_row_upper_lines = ["--------|-------|--------"]
    board_row_2 = [' ', 4, '|', 5, '|', 6, ' ']
    board_row_lower_lines = ["--------|-------|--------"]
    board_row_3 = [' ', 1, '|', 2, '|', 3, ' ']
    def show_board ():
        print(board_row_1)
        print(board_row_upper_lines)
        print(board_row_2)
        print(board_row_lower_lines)
        print(board_row_3)
    show_board()
    number_of_round = 0
    acceptable_pick_range = [1,2,3,4,5,6,7,8,9]
    game_on = True
    while game_on == True:
        if number_of_round % 2 == 0:
            print("Player 1 with X shall pick! \n")
            print("Pick a place on the board between 1 and 9.")
            current_symbol = 'X'
        else:
            print("Player 2 with O shall pick! \n")
            print("Pick a place on the board between 1 and 9.")
            current_symbol = 'O'
        #CHECKING FOR DIGITS, RANGE, AND AVAILABILITY IN SET RANGE
        digit = False
        while digit != True:
            player_pick = input("Pick: ")
            if player_pick.isdigit() and int(player_pick) in acceptable_pick_range:
                print(f"Your pick is: {player_pick}")
                eliminate_choice_from_lst = acceptable_pick_range.index(int(player_pick))
                acceptable_pick_range.pop(eliminate_choice_from_lst)
                print(acceptable_pick_range)
                print(number_of_round)
                digit = True
            else:
                print("Incorrect! Please pick a number within range: 1-9. Make sure it is not already occupied!")
        #REPLACE

        if int(player_pick) in [7,8,9]:
            replace_index = board_row_1.index(int(player_pick))
            board_row_1[replace_index] = current_symbol

        elif int(player_pick) in [4,5,6]:
            replace_index = board_row_2.index(int(player_pick))
            board_row_2[replace_index] = current_symbol

        elif int(player_pick) in [1,2,3]:
            replace_index = board_row_3.index(int(player_pick))
            board_row_3[replace_index] = current_symbol
    
        show_board()
        #WINNING CONDITIONS
        def is_won():
            if board_row_1.count(current_symbol) == 3:
                return True
            elif board_row_2.count(current_symbol) == 3:
                return True
            elif board_row_3.count(current_symbol) == 3:
                return True
            elif board_row_1[1] == board_row_2[1] == board_row_3[1]:
                return True
            elif board_row_1[3] == board_row_2[3] == board_row_3[3]:
                return True
            elif board_row_1[5] == board_row_2[5] == board_row_3[5]:
                return True
            elif board_row_1[1] == board_row_2[3] == board_row_3[5]:
                return True
            elif board_row_1[5] == board_row_2[3] == board_row_3[1]:
                return True
            else:
                return False
        if is_won() == True:
            print(f"{current_symbol} Has won! ")
            game_on = False
            if replay() == True:
                game()
            else:
                print("ByeBye!")
        else:
            number_of_round += 1

game_start()
game()
