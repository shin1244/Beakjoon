import sys
input = sys.stdin.readline

n = int(input())
vecter = [list(map(int, input().strip())) for _ in range(n)]
answer = ''

def cut(Xstart, Xend, Ystart, Yend):
    Xmid = (Xstart + Xend) // 2
    Ymid = (Ystart + Yend) // 2
    check = vecter[Xstart][Ystart]
    if all(vecter[i][j] == check for i in range(Xstart, Xend) for j in range(Ystart, Yend)):
        return str(check)
    
    result = '('
    result += cut(Xstart, Xmid, Ystart, Ymid)
    result += cut(Xstart, Xmid, Ymid, Yend)
    result += cut(Xmid, Xend, Ystart, Ymid)
    result += cut(Xmid, Xend, Ymid, Yend)
    result += ')'
    return result

print(cut(0, n, 0, n))