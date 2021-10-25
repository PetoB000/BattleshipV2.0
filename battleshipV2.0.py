import time, os
import string

def start_menu():
    print(
"""



        Hi, and welcome to the Battleship game!

  

                                        The board size is 5 x 5.

                                        You have to place 2 small ships(2x1) and 2 big ships (2x2) by giving the coordinates.

                                        The faster who find the other player's ships is the winner!


        Please choose from the following options:

                \ \_____
                ###[==_____>  1. Play Battleship Human vs. Human
                /_/      __
                            \ \_____
                        ###[==_____  > 2. Quit
                            /_/



""")

# ha kivalasztotta a jatekomodot ES felrakta a sajat hajoit feljon ez a 2. ASCII  sleep 3 sec aztan indul a lovoldozo fazis

"""
Let's play!
     ....
         ,''. :   __
             \|_.'  `:       _.----._//_
            .'  .'.`'-._   .'  _/ -._ \)-.----O
           '._.'.'      '--''-'._   '--..--'-`
            .'.'___    /`'---'. / ,-'`
ssss      _<__.-._))../ /'----'/.'_____:'.
   \_    :            \ ]              :  '.
     \___:             \\              :    '.
         :              \\__           :    .'
         :_______________|__]__________:  .'
                    .' __ '.           :.'
                  .' .'  '. '.
                .' .'      '. '.
              .' .'          '. '.
           _.' .'______________'. '._
          [_0______________________0_]
          
          
          """


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




if __name__ == "__main__":
    battleship_main()