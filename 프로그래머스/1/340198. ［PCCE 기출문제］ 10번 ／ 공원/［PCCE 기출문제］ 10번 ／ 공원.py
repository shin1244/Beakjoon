def solution(mats, park):
    lenCol = len(park)
    lenRow = len(park[0])
    DP = [[0 for _ in range(lenRow)] for _ in range(lenCol)]

    for i in range(lenCol):
        if park[i][0] == "-1":
            DP[i][0] = 1
    for i in range(lenRow):
        if park[0][i] == "-1":
            DP[0][i] = 1
    
    for i in range(1, lenCol):
        for j in range(1, lenRow):
            if park[i][j] == "-1":
                DP[i][j] = min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]) + 1
    
    maxVal = max(max(row) for row in DP)
    for i in sorted(mats, reverse=True):
        if maxVal >= i:
            return i
    return -1