def solution(board, h, w):
    height = len(board)
    width = len(board[0])
    result = 0

    for y, x in [[-1, 0], [1, 0], [0,-1], [0,1]]:
        if 0 <= h+y < height and 0 <= w+x < width:
            if board[h][w] == board[h+y][w+x]:
                result += 1

    return result