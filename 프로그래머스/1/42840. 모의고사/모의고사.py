def solution(answers):
    S1 = [1, 2, 3, 4, 5]
    S2 = [2, 1, 2, 3, 2, 4, 2, 5]
    S3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    A1, A2, A3 = 0,0,0
    result = []
    for i in range(len(answers)):
        if answers[i] == S1[i%5]:
            A1 += 1
        if answers[i] == S2[i%8]:
            A2 += 1
        if answers[i] == S3[i%10]:
            A3 += 1
    for j in range(len([A1,A2,A3])):
        if max([A1,A2,A3]) == [A1,A2,A3][j]:
            result.append(j+1)
    
    return result
