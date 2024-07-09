from collections import deque

def solution(order):
    result = []
    stack = []
    q = deque(order)
    
    for i in range(1, len(q)+1):
        if i == q[0]:
            result.append(i)
            q.popleft()
            while stack and stack[-1] == q[0]:
                result.append(stack[-1])
                q.popleft()
                stack.pop()
        else:
            stack.append(i)
            
    return len(result)