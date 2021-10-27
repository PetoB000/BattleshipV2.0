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
        option = input("1.Play Battleship Human vs. Human\n2.Quit\n\n")
        if option in ["1","2"]:
            if option == "1":
                clear()
                f = open("logo.txt", "r")
                print(f.readline())
                time.sleep(3)
                f.close()
            if option == "2":
                sys.exit()
        else:
            print("Please choose a number from the menu!\n\n")
            continue
menu()


def init_board(size):
    board = [["0" for _ in range(size)] for _ in range(size)]
    return board


def ask_direction():
    while True:
        direction = input("Horizontal or vertical? ")   # ide kell majd egy feltétel attól függően mekkore flottát tesz le
        if direction.lower() == "h" or direction.lower() == "v":
            return direction
        else:
            print("It is not valid, please try again!")
            continue


def ask_for_fleets():
    valid_moves = get_valid_moves(size=5)[2]
    print(valid_moves)
    while True:
        fleet_input = input("Please place your fleets: ")
        if fleet_input.upper() in valid_moves:
            return fleet_input.upper()
        if fleet_input not in valid_moves:
            print("Not a valid move, please try again! ")
            continue


def convert_input_to_coordinates(coord):
    valid_numbers, valid_letters = get_valid_moves(size=5)[0], get_valid_moves(size=5)[1]
    row_index, col_index = coord[0], coord[1:]
    row = valid_letters.index(row_index)
    col = valid_numbers.index(col_index)
    return row, col



def placement_phase(board, size):
    if size == 5:
        fleets = {2: 2, 2: 1}
        placing_status = 'placing fleets'

    while placing_status == 'placing fleets':          
        fleet_input = ask_for_fleets()
        direction = ask_direction()
        row, col = convert_input_to_coordinates(fleet_input)
        if direction == "h":
            if col < size - 1:
                board[row][col] = '■'
                board[row][col+1] = '■'
                display_board(board)
            else:
                print("Invalid placement, pls try again!")
                direction = ask_direction() 
        print(board, fleet_input, direction, row, col)
        placing_status = 'exit'
    


def display_board(board):
    abc_letters_up = string.ascii_uppercase
    for number in range(len(board)+1):
        print(' ' if number == 0 else number, end=' ')
    print('')
    for row in range(len(board)+1):
        for col in range(len(board)+1):
            print(abc_letters_up[row] if col == 0 else 'O', end=' ')
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



def get_shoot():
    letters, numbers = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4}, {'1':0, '2':1, '3':2, '4':3, '5':4}
    while True:
        move = input("Give a coordinate:").upper()
        if move[0].isalpha() and move[1].isnumeric():
            if len(move) < 3:
                if move[0] in letters and move[1] in numbers:
                    row, col = letters[move[0]], numbers[move[1]]
                    return row, col
                print('Given coordinates are out of field')
            print("Invalid input")
        print("Invalid input")


def battleship_main():
    menu()       #5*5-ös pálya ( 2*2 flotta, meg 2*1 flotta ), plusz üdvözlés, meg egy kilépési lehetőség    >  Marcsi
    board = init_board(size=5)      # pálya létrehozása              
    display_board(board)       # pálya megjelenítése    > Marci
    placement_phase(board, size=5)
        # ask_fleets()                                      > Zsu
        # validate_coordinates()

    # get_shoot()
        # input kérés 
        # validate coordinates()                           > Balázs
        # return row col 

    # hit_confirm(board1, board2, row, col)               > Balázs 
    # game_logic()                                          > az egész csapat
    pass

if __name__ == "__main__":
    battleship_main()