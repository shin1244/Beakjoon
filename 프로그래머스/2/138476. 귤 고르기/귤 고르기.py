from collections import *

def solution(k, tangerine):
    a = Counter(tangerine)
    result = sorted(tangerine, key=lambda x: (a[x], x))
    return len(set(result[-k:]))