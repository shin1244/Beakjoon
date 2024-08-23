from collections import deque

def solution(progresses, speeds):
    result = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        c = 0
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            c += 1
        if c: result.append(c)
    return result
            