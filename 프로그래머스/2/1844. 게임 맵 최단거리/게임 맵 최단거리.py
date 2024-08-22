from heapq import *

def solution(maps):
    len_y = len(maps)
    len_x = len(maps[0])
    
    h = [[1,0,0]]
    heapify(h)
    
    while h:
        c, y, x = heappop(h)
        for ny, nx in [[1,0],[-1,0],[0,1],[0,-1]]:
            if 0 <= y + ny < len_y and 0 <= x + nx < len_x and maps[y+ny][x+nx] == 1:
                if y+ny == len_y-1 and x+nx == len_x-1:
                    return c+1
                maps[y+ny][x+nx] = 0
                heappush(h, [c+1, y+ny, x+nx])
    return -1