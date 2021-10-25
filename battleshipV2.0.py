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
    while True:
        fleet_placement = input("Please place you fleets: ")
        if fleet_placement not in valid_moves:
            print("Not a valid move, please try again! ")
            continue
        elif fleet_placement in valid_moves:
            return fleet_placement


            


def placement_phase(board):
    print(board)
    fleet_placement = ask_for_fleets()
    direction = ask_direction()
    pass





def battleship_main():
    # start menu()       5*5-ös pálya ( 2*2 flotta, meg 2*1 flotta ), plusz üdvözlés, meg egy kilépési lehetőség    >  Marcsi
    board = init_board(size=5)      #pálya létrehozása              
    # display_init_board(board)       pálya megjelenítése    > Marci
    placement_phase(board)
        # ask_fleets()                                      > Zsu
        # validate_coordinates()

    # get_shoot()
        # input kérés 
        # validate coordinates()                           > Balázs
        # return row col 

    # hit_confirm(board1, board2, row, col)               > Balázs 
    # game_logic()                                          > az egész csapat
    




if __name__ == "__main__":
    battleship_main()