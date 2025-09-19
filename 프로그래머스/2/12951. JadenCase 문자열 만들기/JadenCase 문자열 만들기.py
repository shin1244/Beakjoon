def solution(s):
    result = ''
    check = 1
    
    for i in s:
        if i == ' ':
            result += ' '
            check = 1
        elif check:
            result += i.upper()
            check = 0
        else:
            result += i.lower()
            
    return result