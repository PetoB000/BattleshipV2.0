import time
import os
import string
import sys
import copy


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    clear()
    print("""



        Welcome to the Battleship game!

  

                    The board size is 5 x 5.

                    You have to place 2 small ships (2x1) and 2 big ships (2x2) by giving the coordinates.

                    The first, who find the other player's ships, is the winner!


        Please choose from the following options:

                            _
                            \ \_______
                        ###[==______   > Press 1 to play Battleship Human vs. Human 
                            /_/             __
                                            \ \_____
                                        ###[==_____  > Press 2 to Quit
                                            /_/



        """)

    while True:
        option = input("Have fun!\n\n")
        if option == "1":
                clear()
                f = open("logo.txt", "r")
                print(f.read())
                time.sleep(3)
                clear()
                break
        if option == "2":
                sys.exit()
        if option not in ["1","2"]:
                print("Please choose a number from the menu!\n\n")
                continue


def init_board(size=5):
    board = [["0" for _ in range(size)] for _ in range(size)]
    return board


def ask_for_fleets():
    valid_moves = get_valid_moves(size=5)[2]
    while True:
        fleet_input = input("Please place your fleets: ")
        if fleet_input.upper() in valid_moves:
            return fleet_input.upper()
        if fleet_input not in valid_moves:
            print("Not a valid move, please try again! ")
            continue


def ask_direction():
    while True:
        direction = input("Horizontal or vertical? ") 
        if direction.lower() == "h" or direction.lower() == "v":
            return direction.lower()
        else:
            print("It is not valid, please try again!")
            continue


def convert_input_to_coordinates(coord):
    valid_numbers, valid_letters = get_valid_moves(size=5)[0], get_valid_moves(size=5)[1]
    row_index, col_index = coord[0], coord[1:]
    row = valid_letters.index(row_index)
    col = valid_numbers.index(col_index)
    return row, col



def checking_valid_fleetplacing_row(board, row_check, col_check):
    table_size = len(board)
    for row in range(table_size):
        for col in range(table_size):
            if row < 1:
                if row_check == row and col_check == col:
                    if board[row+1][col] == '■':
                        return False
                    return True
            elif row >= 1 and row < table_size - 1:
                if row_check == row and col_check == col:
                    if board[row-1][col] == '■':
                        return False
                    elif board[row+1][col] == '■':
                        return False
                    return True
                continue
            else:
                if row_check == row and col_check == col:
                    if board[row-1][col] == '■':
                        return False
                    return True


def checking_valid_fleetplacing_col(board, row_check, col_check):
    table_size = len(board) 
    for row in range(table_size):
        for col in range(table_size):
            if col >= 1 and col < table_size - 1:
                if row_check == row and col_check == col:
                    if board[row][col-1] == '■':
                        return False
                    elif board[row][col+1] == '■':
                        return False
                    return True
                continue
            elif col < 1:
                if row_check == row and col_check == col:
                    if board[row][col+1] == '■':
                        return False
                    return True
            else:
                if row_check == row and col_check == col:
                    if board[row][col-1] == '■':
                        return False
                    return True


def fillup_fleet_pos_dict(coordinates):
    fleets = {}
    count = 1
    for element in coordinates:
        fleets[count] = element
        count += 1
    return fleets


def checking_direction_while_placing(board, direction, row, col):
    pass


def placing_2_block_long_ship(board, size, value):
    fleet_positions = []
    while value != 0:                          
        fleet_input = ask_for_fleets()
        direction = ask_direction()
        row, col = convert_input_to_coordinates(fleet_input)
        if direction == "h":
            if col < size - 1:
                if checking_valid_fleetplacing_row(board, row, col) and checking_valid_fleetplacing_col(board, row, col):
                    if checking_valid_fleetplacing_row(board, row, col+1) and checking_valid_fleetplacing_col(board, row, col+1):
                        board[row][col] = '■'
                        board[row][col+1] = '■'
                        coordinates = [(row, col), (row, col+1)]
                        fleet_positions.append(coordinates)
                        clear()
                        display_board(board)
                        value -= 1
                    else:
                        print("Invalid placement, you can not place your fleet next to yours another one, pls try again!")
                        continue
                else:
                    print("Invalid placement, you can not place your fleet next to yours another one, pls try again!")
                    continue
            else:
                print("Invalid placement, pls try again!")
                continue
        if direction == "v":
            if row < size -1:
                if checking_valid_fleetplacing_row(board, row, col) and checking_valid_fleetplacing_col(board, row, col):
                    if checking_valid_fleetplacing_row(board, row+1, col) and checking_valid_fleetplacing_col(board, row+1, col):
                        board[row][col] = '■'
                        board[row+1][col] = '■'
                        coordinates = [(row, col), (row+1, col)]
                        fleet_positions.append(coordinates)
                        clear()
                        display_board(board)
                        value -= 1
                    else:
                        print("Invalid placement, you can not place your fleet next to yours another one, pls try again!")
                        continue                         
                else:
                    print("Invalid placement, you can not place your fleet next to yours another one, pls try again!")
                    continue                    
            else:
                print("Invalid placement, pls try again!")
                continue
    return board, fleet_positions


def placing_1_block_long_ship(board, value):
    while value != 0:                          
        fleet_input = ask_for_fleets()
        row, col = convert_input_to_coordinates(fleet_input)
        if board[row][col] == '■':
            print("The field already taken, pls try again!")
            continue
        else:
            if checking_valid_fleetplacing_row(board, row, col) and checking_valid_fleetplacing_col(board, row, col):
                board[row][col] = '■'
                clear()
                display_board(board)
                value -= 1
            else:
                print("Invalid placement, you can not place your fleet next to yours another one, pls try again!")
                continue
    return board


def placement_phase(board, size=5):
    if size == 5:
        fleets = {"2 block long ship": 2, "1 block long ship": 2}
        placing_status = 'placing fleets'

    while placing_status == 'placing fleets':
        for key, value in fleets.items():
            if key == "2 block long ship":
                board, fleet_positions = placing_2_block_long_ship(board, size, value)
            if key == "1 block long ship":
                board = placing_1_block_long_ship(board, value)
        placing_status = 'exit'
    
    return board, fleet_positions             


def display_board(board):
    abc_letters_up = string.ascii_uppercase
    for number in range(len(board)):
        if number == 0:
            print('  ' + str(number+1), end = ' ')
        else:
            print(str(number+1), end = ' ')
    print('')
    for row in range(len(board)):
        for col in range(len(board)):
            if col == 0:
                print(abc_letters_up[row]+ ' '+board[row][col], end=' ')
            else:
                print(board[row][col], end=' ')
        print('')
    print('')


def board_value_converter(fleet_board, hidden_board):
    board_lenght = len(fleet_board)
    for row in range(board_lenght):
        for col in range(board_lenght):
            if fleet_board[row][col] != '■':
                hidden_board[row][col] = fleet_board[row][col]
    return hidden_board


def display_hidden_board(board1, board2):
    board_lenght = len(board1)
    abc_letters_up = string.ascii_uppercase
    print("  1 2 3 4 5\t\t\t\t  1 2 3 4 5")
    for i in range(board_lenght):
        print(f"{abc_letters_up[i]} {board1[i][0]} {board1[i][1]} "
              f"{board1[i][2]} {board1[i][3]} {board1[i][4]}"
              f"\t\t\t\t{abc_letters_up[i]} {board2[i][0]} "
              f"{board2[i][1]} {board2[i][2]} {board2[i][3]} {board2[i][4]}")


def get_valid_moves(size=5):
    abc_letters = string.ascii_uppercase
    valid_letters = []
    for letter in range(size):
        valid_letters.append(abc_letters[letter])
    valid_numbers = []
    for number in range(size):
        valid_numbers.append(str(number+1))
    valid_letters_and_numbers = []
    for letter in range(size):
        for number in range(size):
            valid_letters_and_numbers.extend([abc_letters[letter],str((number+1))])
    valid_moves = []
    for i in range(0,len(valid_letters_and_numbers),2):
            if i<len(valid_letters_and_numbers)-1:
                valid_moves.append(valid_letters_and_numbers[i]+valid_letters_and_numbers[i+1])

    return valid_numbers, valid_letters, valid_moves


def get_player(player):
    if player == "Player1":
        player = "Player2"
    else:
        player = "Player1"
    return player 


def get_shoot():
    """Asks for user input for the shot until the input is valid."""
    valid_moves = get_valid_moves(size=5)[2]
    while True:
        move = input("Give a coordinate:").upper()
        if move[0].isalpha() and move[1].isnumeric():
            if len(move) < 3:
                if move in valid_moves:
                    row, col = convert_input_to_coordinates(move)
                    return row, col
                print('Given coordinates are out of field')
            else:
                print("Invalid input")
        else:
            print("Invalid input")


def hit_checking_around_row(board, row, col):
    table_size = len(board)
    if row < 1:
        if board[row+1][col] != '■':
            if board[row+1][col] == 'H':
                board[row][col] = 'S'
                board[row+1][col] = 'S'
                return True, board
        elif board[row+1][col] == '■':
            pass
    elif row >= 1 and row < table_size - 1:
        pass


def hit_function(board, row_shoot, col_shoot, fleet_pos):
    for row in range(len(board)):   # nem biztos hogy kell a dupla for ciklus?
        for col in range(len(board)):
            if row == row_shoot and col == col_shoot:
                if board[row][col] == '0':
                    print("It's a MISS!!")
                    board[row][col] = 'M'
                    return board
                elif board[row][col] == 'M' or board[row][col] == 'S'or board[row][col] == 'H':
                    print("Too bad.. You have already shooted this field.. It's a MISS again!!")
                    return board                    
                elif board[row][col] == '■':
                    for item in fleet_pos:
                        for element in item:
                            hit_list = []
                            hit_list = item.copy()
                            #hit_list.append(item)
                            print(hit_list, item, element)
                            if element == (row, col):
                                hit_list.remove(element)
                                row_check, col_check = hit_list[0][0], hit_list[0][1]
                                print(row_check, col_check)
                                if board[row_check][col_check] == '■':   #hit 2 blocks ship
                                    print("It's a hit!!!")
                                    board[row][col] = 'H'
                                    return board
                                elif board[row_check][col_check] == 'H':
                                    print("It's a hit!!!\nShip sunk!!!")
                                    board[row][col], board[row_check][col_check] = 'S', 'S'
                                    return board
                            hit_list = []
                    print("It's a hit!!!\nShip sunk!!!")  # hit one block ship
                    board[row][col] = 'S'
                    return board
                                               

def has_won(board, size=5):
    count_s_element = 0
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 'S':
                count_s_element += 1
    if size == 5:
        if count_s_element == 6:
            return True
    return False


def game_result(player):
    print(f'Congratulations, {player} is the winner!')


def play_again():
    while True:
        again = input('Would you like to play again?\nPlease choose Y or N: ').upper()
        if again == 'Y':
            battleship_main()
        elif again == 'N':
            sys.exit()
        else:
            print('Please choose Y or N!')
            continue


def play_sequence():    
    sequence = 0
    for sequence in range (100):
        if sequence % 2 == 0:
            hit_function("player1",sequence)            
        else:    
            get_shoot("player2",sequence)
    pass


def battleship_main():
    menu()       
    player_1_board, player_2_board = init_board(), init_board()
    hidden_board_1, hidden_board_2 = init_board(), init_board()
    counter = 50
    clear()
    display_board(player_1_board)
    player_1_board, fleets_player1 = placement_phase(player_1_board)
    clear()
    display_board(player_2_board)
    player_2_board, fleets_player2 = placement_phase(player_2_board)
    p_1_turn = counter//2
    p_2_turn = counter//2
    player = 'Player2'
    while counter != 0:
        clear()
        converted_h_board1 = board_value_converter(player_1_board, hidden_board_1)
        converted_h_board2 = board_value_converter(player_2_board, hidden_board_2)
        player = get_player(player)
        if player == 'Player1':
            print(f"\t\t{player}'s turn\n\t\t{p_1_turn} turn(s) left ")
            display_hidden_board(converted_h_board1, converted_h_board2)
            row, col = get_shoot()
            player_2_board = hit_function(player_2_board, row, col, fleets_player1)
            time.sleep(2)
            if has_won(player_2_board):
                game_result(player)
                play_again()
            p_1_turn -= 1
        else:
            print(f"\t\t{player}'s turn\n\t\t{p_2_turn} turn(s) left ")
            display_hidden_board(converted_h_board1, converted_h_board2)
            row, col = get_shoot()
            player_1_board = hit_function(player_1_board, row, col, fleets_player2)
            time.sleep(2)
            if has_won(player_1_board):
                game_result(player)
                play_again()
            p_2_turn -= 1
        counter -= 1
    print("It's a draw!")
    play_again()


if __name__ == "__main__":
    battleship_main()