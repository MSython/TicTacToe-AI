from algorithms import minimax , checkWining

board = [
    0, 1, 2,
    3, 4, 5,
    6, 7, 8
]

humanPlayer = "O"
computerPlayer = "X"

player = computerPlayer
for i in range(9):
    if not checkWining(board,player):
        if player == computerPlayer:
            move = minimax(board,computerPlayer)
            board[move['index']] = player
            player = humanPlayer
        else:
            print(f"""{board[0]} | {board[1]} | {board[2]}
---------            
{board[3]} | {board[4]} | {board[5]}
---------            
{board[6]} | {board[7]} | {board[8]}
---------            """)
            move = input(": ")
            board[int(move)] = humanPlayer
            player = computerPlayer
    else:
        break
