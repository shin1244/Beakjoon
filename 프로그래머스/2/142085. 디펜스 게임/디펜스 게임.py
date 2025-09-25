import heapq

def solution(n, k, enemy):
    heap = []
    total = 0
    answer = 0

    for e in enemy:
        heapq.heappush(heap, -e)
        total += e
        if total > n:
            if k == 0:
                break
            total += heapq.heappop(heap)
            k -= 1
        answer += 1
    return answer