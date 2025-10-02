from collections import Counter

def solution(weights):
    result = 0

    wc = Counter(weights)
    r = [(1,1),(1,2),(3,2),(4,3)]

    for w in wc:
        for a, b in r:
            t = w*a/b
            if t in wc:
                if t == w:
                    result += wc[w] * (wc[w] - 1) // 2
                else:
                    result += wc[w] * wc[t]

    return result