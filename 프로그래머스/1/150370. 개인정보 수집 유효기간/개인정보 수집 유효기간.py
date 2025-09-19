def solution(today, terms, privacies):
    year, month, day = map(int, today.split("."))
    termMap = {}
    result = []

    for t in terms:
        ts = t.split(" ")
        termMap[ts[0]] = int(ts[1])

    for idx in range(len(privacies)):
        userToday, term = privacies[idx].split(" ")
        userYear, userMonth, userDay = map(int, userToday.split("."))

        userMonth += termMap[term]
        userYear += (userMonth - 1) // 12
        userMonth = (userMonth - 1) % 12 + 1

        userDay -= 1
        if userDay == 0:
            userMonth -= 1
            if userMonth == 0:
                userYear -= 1
                userMonth = 12
            userDay = 28

        if (userYear, userMonth, userDay) < (int(year), int(month), int(day)):
            result.append(idx+1)
    
    return result