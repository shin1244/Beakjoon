def solution(n, computers):
    result = 0
    visited = []
    
    for i in range(n):
        if i not in visited:
            result += 1
            visited.append(i)
            
            arr = [computers[i]]
            while arr:
                now = arr.pop()
                for j in range(n):
                    if now[j] == 1 and j not in visited:
                        visited.append(j)
                        arr.append(computers[j])
                        
    return result