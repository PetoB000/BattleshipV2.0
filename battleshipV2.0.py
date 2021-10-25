def init_board(size):
    board = [["0" for _ in range(size)] for _ in range(size)]
    return board






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