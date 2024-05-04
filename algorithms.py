humanPlayer = "O"
computerPlayer = "X"

def getEmpty(board: list):
    emptys = []
    for i in range(len(board)):
        if board[i] != "X" and board[i] != "O":
            emptys.append(board[i])
    return emptys

def checkWining(board,player): # -> check player winned
    if (
            (board[0] == player and board[1] == player and board[2] == player) or
            (board[3] == player and board[4] == player and board[5] == player) or
            (board[6] == player and board[7] == player and board[8] == player) or
            (board[0] == player and board[3] == player and board[6] == player) or
            (board[1] == player and board[4] == player and board[7] == player) or
            (board[2] == player and board[5] == player and board[8] == player) or
            (board[0] == player and board[4] == player and board[8] == player) or
            (board[2] == player and board[4] == player and board[6] == player)
    ):
        return True
    return False

def minimax(newBoard,player):
    availSpots = getEmpty(newBoard) # -> get available spots

    if checkWining(newBoard,humanPlayer):
        return {"score":-10}
    elif checkWining(newBoard,computerPlayer):
        return {"score":10}
    elif len(availSpots) == 0:
        return {"score": 0}

    if len(availSpots) == 9:
        return {"index": 4}
    # elif len(availSpots) == 8:
    #     choises = []
    #     for i in [1,3,5,7] :
    #         choises.append(i)
    #     return {"index": random.choice(choises)}


    moves = []
    for i in range(len(availSpots)):
            move = {}
            move["index"] = newBoard[availSpots[i]]
            newBoard[availSpots[i]] = player
            if player == computerPlayer:
                result = minimax(newBoard,humanPlayer)
                move['score'] = result['score']
            else:
                result = minimax(newBoard, computerPlayer)
                move['score'] = result['score']
            newBoard[availSpots[i]] = move["index"];
            moves.append(move)

    if (player == computerPlayer):
        bestScore = -10000
        for i in range(len(moves)):
            if moves[i]["score"] > bestScore:
                bestScore = moves[i]['score']
                bestMove = i
    elif (player == humanPlayer):
        bestScore = 1000
        for i in range(len(moves)):
            if moves[i]["score"] < bestScore:
                bestScore = moves[i]["score"]
                bestMove = i

    return moves[bestMove]