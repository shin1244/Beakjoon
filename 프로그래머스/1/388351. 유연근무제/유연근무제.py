def solution(schedules, timelogs, startday):
    result = 0
    for idx, schedule in enumerate(schedules):
        schedules[idx] = changeMin(schedule) + 10


    for pIdx,timelog in enumerate(timelogs):
        check = True
        for dayIdx, log in enumerate(timelog):
            if ((startday+dayIdx) % 7 != 0 and (startday+dayIdx) % 7 != 6) and schedules[pIdx] < changeMin(log):
                check = False
                break
        if check:
            result += 1
    
    return result



def changeMin(time):
    hour = time // 100
    min = (60 * hour) + (time % 100)

    return min