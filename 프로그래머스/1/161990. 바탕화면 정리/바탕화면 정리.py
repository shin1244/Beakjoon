def solution(wallpaper):
    result = [0,0,0,0]
    x = len(wallpaper[0])
    y = len(wallpaper)
    for idx,row in enumerate(wallpaper):
        for val in row:
            if val == "#":
                result[2] = idx + 1
                break
    
    for j in range(x):
        for i in range(y):
            if wallpaper[i][j] == "#":
                result[3] = j + 1
                break

    for i in range(y-1, -1, -1):
        for j in range(x):
            if wallpaper[i][j] == "#":
                result[0] = i
                break
    
    for j in range(x-1, -1, -1):
        for i in range(y):
            if wallpaper[i][j] == "#":
                result[1] = j
                break

    return result