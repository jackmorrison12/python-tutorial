def tic_tac_toe():

    # Question 1
    # TODO: Create the board as a 3x3 2D array
    #       Initialise it with numbers 1-9

    WIN_COMBINATIONS = [
       ((0,0), (0,1), (0,2)),
       ((1,0), (1,1), (1,2)),
       ((2,0), (2,1), (2,2)),
       ((0,0), (1,1), (2,2)),
       ((0,2), (1,1), (2,0)),
       ((0,0), (1,0), (2,0)),
       ((0,1), (1,1), (2,1)),
       ((0,2), (1,2), (2,2))
    ]

    def draw():
        # Question 2
        # TODO: Print out the contents of the board
        print()

    def choose_number():
        while True:
            try:
                a = int(input())
                if a in range(1,10):
                    return a
                else:
                    print("\nInvalid move. Try again")
            except ValueError:
               print("\nThat's not a number. Try again")

    def is_game_over():
        for (a1,a2), (b1,b2), (c1,c2) in WIN_COMBINATIONS:
            if board[a1][a2] == board[b1][b2] == board[c1][c2]:
                print("Player {0} wins!\n".format(board[a1][a2]))
                print("Congratulations!\n")
                return True

        # Question 3
        # TODO: Check to see if the board is full, so it is a tie 
        # (HINT: Iterate over the board array and sum up how many X or 0s 
        # there are. If there are 9, tell them it was a tie and return True)

    for player in 'XO' * 9:
        draw()
        if is_game_over():
            break
        print("Player {0} pick your move".format(player))
        num = choose_number()
        board[(num - 1) // 3][num % 3 - 1] = player
        print()

while True:
    tic_tac_toe()
    if input("Play again (y/n)\n") != "y":
        break