import time
import os
import string


def clear():
    os.system("clear")

def init_board(size):
    board = [["0" for _ in range(size)] for _ in range(size)]
    return board


def display_board(board):
    abc_letters_up = string.ascii_uppercase
    for number in range(len(board)+1):
        print(' ' if number == 0 else number, end=' ')
    print('')
    for row in range(len(board)+1):
        for col in range(len(board)+1):
            print(abc_letters_up[row] if col == 0 else 'O', end=' ')
        print('')


def validate_coordinates(size):
    abc_letters = string.ascii_uppercase
    validate_letters_numbers = [] 
    for letter in range(size):
        validate_letters_numbers.extend([abc_letters[letter], letter])

    return validate_letters_numbers

def get_shoot():
    move = input("Give a coordinate:")
    valid = validate_coordinates()
    if valid == True:
        row, col = move[0], move[1]
        return row, col

def battleship_main():
    # start menu()       5*5-ös pálya ( 2*2 flotta, meg 2*1 flotta ), plusz üdvözlés, meg egy kilépési lehetőség    >  Marcsi
    # board = init_board(size=5)      pálya létrehozása              
    # display_init_board(board)       pálya megjelenítése    > Marci
    # placement_phase(board1, board2)
        # ask_fleets()                                      > Zsu
        # validate_coordinates()

    # get_shoot()
        # input kérés 
        # validate coordinates()                           > Balázs
        # return row col 

    # hit_confirm(board1, board2, row, col)               > Balázs 
    # game_logic()                                          > az egész csapat
        pass

def menu():
    os.system("clear")
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
    if input == 1:
        display_board(board)
    if input == 2:
        os.exit
        print("Please choose a number from the menu!\n\n")
        continue
    break

menu()


if __name__ == "__main__":
    battleship_main()