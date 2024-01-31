from heapq import *

def find(arr,n):
    if arr[n] == n:
        return arr[n]
    arr[n] = find(arr, arr[n])
    return arr[n]

def union(arr, a, b):
    root_a = find(arr, a)
    root_b = find(arr, b)
    arr[root_b] = root_a

def solution(n, costs):
    arr = [i for i in range(n)]
    costs = [list(reversed(i)) for i in costs]
    heapify(costs)
    result = 0
    while costs:
        value, end, start = heappop(costs)
        find_start, find_end = find(arr, start), find(arr, end)
        if find(arr, start) != find(arr, end):
            result += value
            union(arr, start, end)
            
    return result