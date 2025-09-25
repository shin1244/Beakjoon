def solution(board):
    rows = len(board)
    cols = len(board[0])
    dp = [[0]*cols for _ in range(rows)]
    max_len = 0

    for y in range(rows):
        for x in range(cols):
            if board[y][x] == 1:
                if y == 0 or x == 0:
                    dp[y][x] = 1
                else:
                    dp[y][x] = min(dp[y-1][x], dp[y][x-1], dp[y-1][x-1])+1
            max_len = max(max_len, dp[y][x])
    return max_len * max_len