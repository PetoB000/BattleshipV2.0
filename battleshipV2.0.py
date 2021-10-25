import string


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