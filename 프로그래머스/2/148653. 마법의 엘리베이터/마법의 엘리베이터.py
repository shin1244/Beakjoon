def solution(storey):
    result = 0
    while storey > 0:
        r = round(storey, -1)
        d = abs(storey - r)
        result += d
        storey = r // 10
    
    return result + storey