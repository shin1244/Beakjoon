import copy

def solution(m, n, board):
    beforeBoard = []
    afterBoard = []
    result = 0
    for y in board:
        beforeBoard.append(list(y))
        afterBoard.append(list(y))
        
    while True:
        for y in range(m-1):
            for x in range(n-1):
                if beforeBoard[y][x] == beforeBoard[y+1][x] == beforeBoard[y+1][x+1] == beforeBoard[y][x+1]:
                    afterBoard[y][x] = ""
                    afterBoard[y+1][x] = ""
                    afterBoard[y+1][x+1] = ""
                    afterBoard[y][x+1] = ""

        for x in range(n):
            c = m-1
            for y in range(m-1, -1, -1):
                if afterBoard[y][x] != "":
                    afterBoard[c][x], afterBoard[y][x] = afterBoard[y][x], afterBoard[c][x]
                    c -= 1

        if beforeBoard == afterBoard:
            for arr in beforeBoard:
                for a in arr:
                    if a == "":
                        result += 1
            return result

        beforeBoard = copy.deepcopy(afterBoard)