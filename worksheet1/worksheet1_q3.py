def tic_tac_toe():
    board = [[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            board[i][j] = (3 * i) + (j + 1)

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
        print(board[0][0], board[0][1], board[0][2])
        print(board[1][0], board[1][1], board[1][2])
        print(board[2][0], board[2][1], board[2][2])
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

        sum = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X' or board[i][j] == '0':
                    sum += 1
        if sum == 9:
            print("The game ends in a tie\n")
            return True

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