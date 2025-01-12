from bisect import *

def solution(A, B):
    B = sorted(B)
    result = 0
    
    for num_A in A:
        idx = bisect_right(B, num_A)
        if idx == len(B):
            continue
        B.pop(idx)
        result += 1
    
    return result