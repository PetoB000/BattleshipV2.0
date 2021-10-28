import time
import os
import string
import sys
import copy


def clear():
    os.system("clear")
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
                # f = open("logo.txt", "r")
                # print(f.read())
                # time.sleep(3)
                # clear()
                break
        if option == "2":
                sys.exit()
        if option not in ["1","2"]:
                print("Please choose a number from the menu!\n\n")
                continue

size = 5
def init_board(size):
    board = [["0" for _ in range(size)] for _ in range(size)]
    return board


def ask_for_fleets():
    valid_moves = get_valid_moves()[2]
    while True:
        fleet_input = input("Please place your fleets: ")
        if fleet_input.upper() in valid_moves:
            return fleet_input.upper()
        if fleet_input not in valid_moves:
            print("Not a valid move, please try again! ")
            continue


def ask_direction():
    while True:
        direction = input("Horizontal or vertical? ")   # ide kell majd egy feltétel attól függően mekkore flottát tesz le
        if direction.lower() == "h" or direction.lower() == "v":
            return direction.lower()
        else:
            print("It is not valid, please try again!")
            continue


def convert_input_to_coordinates(coord):
    valid_numbers, valid_letters = get_valid_moves()[0], get_valid_moves()[1]
    row_index, col_index = coord[0], coord[1:]
    row = valid_letters.index(row_index)
    col = valid_numbers.index(col_index)
    return row, col

#refactor
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


def placing_2_block_long_ship(board, size, value, fleet_positions):
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
                        key, val = 2, ((row, col), (row, col+1))
                        dict_update = {key: val}
                        fleet_positions.update(dict_update)
                        print(fleet_positions)
                        display_board(board)
                        print(board, fleet_input, direction, row, col)
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
                    if checking_valid_fleetplacing_row(board, row, col) and checking_valid_fleetplacing_col(board, row+1, col):
                        board[row][col] = '■'
                        board[row+1][col] = '■'
                        display_board(board)
                        print(board, fleet_input, direction, row, col)
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
    return board


def placing_1_block_long_ship(board, value, fleet_positions):
    while value != 0:                          
        fleet_input = ask_for_fleets()
        row, col = convert_input_to_coordinates(fleet_input)
        if board[row][col] == '■':
            print("The field already taken, pls try again!")
            continue
        else:
            if checking_valid_fleetplacing_row(board, row, col) and checking_valid_fleetplacing_col(board, row, col):
                board[row][col] = '■'
                display_board(board)
                value -= 1
            else:
                print("Invalid placement, you can not place your fleet next to yours another one, pls try again!")
                continue
    return board


def placement_phase(board, size):
    if size == 5:
        fleets = {"2 block long ship": 2, "1 block long ship": 2}
        fleet_positions = {}
        placing_status = 'placing fleets'

    while placing_status == 'placing fleets':
        for key, value in fleets.items():
            if key == "2 block long ship":
                board = placing_2_block_long_ship(board, size, value, fleet_positions)
            if key == "1 block long ship":
                board = placing_1_block_long_ship(board, value, fleet_positions)
        placing_status = 'exit'
    
    return board             


def display_board(board):
    # abc_letters_up = string.ascii_uppercase
    # print("  1 2 3 4 5\t\t\t\t  1 2 3 4 5")
    # for row in range(len(board1)):
    #     for col in range(1):
    #         print(f"{abc_letters_up[i]} {board1[row][col]} {board2[row][col]} "
    #               f"{board[i][col]} {board[i][col]} {board[i][col]}"
    #               f"\t\t\t\t{abc_letters_up[i]} {board[i][col]} "
    #               f"{board[i][col]} {board[i][col]} {board[i][col]} {board[i][col]}")
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
    if player == "player1":
        player = "player2"
    else:
        player = "player1"
    return player


def get_shoot():
    """Asks for user input for the shot until the input is valid."""
    valid_moves = get_valid_moves()[2]
    while True:
        move = input("Give a coordinate:").upper()
        if move[0].isalpha() and move[1].isnumeric():
            if len(move) < 3:
                if move in valid_moves:
                    row, col = convert_input_to_coordinates(move)
                    return row, col
                print('Given coordinates are out of field')
            print("Invalid input")
        print("Invalid input")


def hit_confirm(board, row, col):
    if board[row][col] == '0':
        board[row][col] = 'M'
        return board
    elif board[row][col] == '■' and board[row][col+1] == 'H':
        board[row][col], board[row][col+1] = 'S', 'S'
        return board
    elif board[row][col] == '■' and board[row][col-1] == 'H':
        board[row][col], board[row][col-1] = 'S', 'S'
        return board
    elif board[row][col] == '■' and board[row+1][col] == 'H':
        board[row][col], board[row+1][col] = 'S', 'S'
        return board
    elif board[row][col] == '■' and board[row-1][col] == 'H':
        board[row][col], board[row-1][col] = 'S', 'S'
        return board
    elif board[row][col] == '■' and board[row][col+1] == '■' or \
        board[row][col] == '■' and board[row][col-1] == '■' or \
        board[row+1][col] == '■' and board[row][col] == '■' or \
        board[row-1][col] == '■' and board[row][col] == '■':
        board[row][col] = 'H'
        return board
    elif board[row][col] == '■' and board[row][col+1] == '0' or \
            board[row][col] == '■' and board[row][col+1] == 'M'or \
            board[row][col] == '■' and board[row][col-1] == '0' or \
            board[row][col] == '■' and board[row][col-1] == 'M' or \
            board[row][col] == '■' and board[row+1][col] == '0' or \
            board[row][col] == '■' and board[row+1][col] == 'M' or \
            board[row][col] == '■' and board[row-1][col] == '0' or \
            board[row][col] == '■' and board[row-1][col] == 'M':
        board[row][col] = 'S'
        return board


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


def hit_function(board, row_shoot, col_shoot):
    # if board[row_shoot][col_shoot] != 
    for row in range(len(board)):
        for col in range(len(board)):
            if row == row_shoot and col == col_shoot:
                if board[row][col] == '0':
                    print("It's a MISS!!")
                    board[row][col] = 'M'
                    return board
                elif board[row][col] == 'M' or board[row][col] == 'S':
                    print("Too bad.. You have already shooted this field.. It's a MISS again!!")
                    return board                    
                elif board[row][col] == '■':
                    if hit_checking_around_row(board, row, col):
                        board = hit_checking_around_row(board, row, col)[1]
                        print("Ship sunk!!!")
                        return board                        
                    board[row][col] = "H"
                    print("It's a hit!!!")
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
        else:
            return False

def game_result(text, player):
    print(f'Congratulations, {player} is the winner!')

def game_logic(board):
    pass


def battleship_main():
    menu()       
    player_1_board, player_2_board = init_board(size=5), init_board(size=5)
    display_board(player_1_board)
    player1, player2 = player_1_board, player_2_board
    counter = 50
    player_1_board = placement_phase(player_1_board, size=5)
    #player_2_board = placement_phase(player_2_board, size=5)
    # display_board(board)
    while counter != 0:
        if counter % 2 == 0:
            #player1
            display_board(player_1_board)
            row, col = get_shoot()
            player_1_board = hit_confirm(player_1_board, row, col) # player2 board kell majd ide
            display_board(player_1_board)
            if has_won(player_1_board):
                pass
            # print player1 won
            #   play again() 
        else:
            #player2
            display_board(player_2_board)
            row, col = get_shoot()
            hit_confirm(player_2_board, row, col)
            if has_won(player_2_board):
                pass
            # print player1 won
            #   play again() 
        counter -= 1

    # print(Its a draw) play again()
    

    # game_logic(player_1_board, player_2_board)                               

if __name__ == "__main__":
    battleship_main()