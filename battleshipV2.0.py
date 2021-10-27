import time
import os
import string
import sys


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

size = 5
def init_board(size):
    board = [["0" for _ in range(size)] for _ in range(size)]
    return board


def ask_for_fleets():
    valid_moves = get_valid_moves()[2]
    print(valid_moves)
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


def checking_right_direction(board, size, value, row, col, direction):
    pass # nem biztos hogy ki kell szervezni..


def placing_2_block_long_ship(board, size, value):
    while value != 0:                          
        fleet_input = ask_for_fleets()
        direction = ask_direction()
        row, col = convert_input_to_coordinates(fleet_input)
        if direction == "h":
            if col < size - 1:
                board[row][col] = '■'
                board[row][col+1] = '■'
                display_board(board)
                print(board, fleet_input, direction, row, col)
                value -= 1
            else:
                print("Invalid placement, pls try again!")
                continue
        if direction == "v":
            if row < size -1:
                board[row][col] = '■'
                board[row+1][col] = '■'
                display_board(board)
                print(board, fleet_input, direction, row, col)
                value -= 1
            else:
                print("Invalid placement, pls try again!")
                continue
    return board


def placing_1_block_long_ship(board, value):
    while value != 0:                          
        fleet_input = ask_for_fleets()
        row, col = convert_input_to_coordinates(fleet_input)
        board[row][col] = '■'
        display_board(board)
        value -= 1
    return board


def placement_phase(board, size):
    if size == 5:
        fleets = {"2 block long ship": 2, "1 block long ship": 2}
        placing_status = 'placing fleets'

    while placing_status == 'placing fleets':
        for key, value in fleets.items():
            if key == "2 block long ship":
                board = placing_2_block_long_ship(board, size, value)
            if key == "1 block long ship":
                board = placing_1_block_long_ship(board, value)
        placing_status = 'exit'
    return board             


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
    valid_letters, valid_numbers = get_valid_moves()[1], get_valid_moves()[0]
    while True:
        move = input("Give a coordinate:").upper()
        if move[0].isalpha() and move[1].isnumeric():
            if len(move) < 3:
                if move[0] in valid_letters and move[1] in valid_numbers:
                    row, col = move[0], move[1]
                    return row, col
                print('Given coordinates are out of field')
            print("Invalid input")
        print("Invalid input")


def hit_confirm(board, row, col):
    if board[row][col] == '■' and board[row][col+1] == 'H':
        board[row][col], board[row][col+1] = 'S'
        return board[row][col], board[row][col + 1]
    elif board[row][col] == '■' and board[row][col+1] == '■':
        board[row][col] = 'H'
        return board[row][col]
    elif board[row][col] == '■' and board[row+1][col] == 'H':
        board[row][col], board[row+1][col] = 'S'
        return board[row][col], board[row+1][col]
    elif board[row+1][col] == '■' and board[row][col] == '■':
        board[row][col] = 'H'
        return board[row][col]
    elif board[row][col] == '■' and board[row][col+1] == '0' or board[row][col+1] == 'M':
        board[row][col] = 'S'
        return board[row][col]
    elif board[row][col] == '■' and board[row+1][col] == '0' or board[row+1][col] == 'M':
        board[row][col] = 'S'
        return board[row][col]


def game_logic(board):
    pass


def battleship_main():
    menu()       
    player_1_board, player_2_board = init_board(size=5), init_board(size=5)
    player1, player2 = player_1_board, player_2_board
    counter = 50
    player_1_board = placement_phase(player_1_board, size=5)
    player_2_board = placement_phase(player_2_board, size=5)
    # display_board(board)
    while counter != 0:
        if counter % 2 == 0:
            #player1
            display_board(player_1_board)
            row, col = get_shoot()
            hit_confirm(player_1_board, row, col)
            # if has_won(player_1_board, size=5):
            # print player1 won
            #   play again() 
        else:
            #player2
            display_board(player_2_board)
            row, col = get_shoot()
            hit_confirm(player_2_board, row, col)
            # if has_won(player_1_board, size=5):
            # print player1 won
            #   play again() 
        counter -= 1

    # print(Its a draw) play again()
    

    # game_logic(player_1_board, player_2_board)                               

if __name__ == "__main__":
    battleship_main()