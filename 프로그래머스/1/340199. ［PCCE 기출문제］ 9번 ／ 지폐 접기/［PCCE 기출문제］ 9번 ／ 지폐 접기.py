def solution(wallet, bill):
    width, height = wallet[0], wallet[1]
    result = 0
    while True:
        if max(width, height) >= max(bill) and min(width, height) >= min(bill):
            return result
        if bill[0] > bill[1]:
            bill[0] = bill[0] // 2
        else:
            bill[1] = bill[1] // 2
        result += 1

