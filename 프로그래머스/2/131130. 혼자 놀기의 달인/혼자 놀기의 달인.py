def solution(cards):
    idx = 0
    check_list = []
    count_list = []
    while len(check_list) != len(cards):
        count = 0
        for i in range(len(cards)+1):
            if i not in check_list:
                idx = i
                
        while idx not in check_list:
            check_list.append(idx)
            idx = cards[idx-1]
            count += 1
        count_list.append(count)
    
    count_list.sort()
    if len(count_list) == 1:
        return 0
    return count_list[-1] * count_list[-2]