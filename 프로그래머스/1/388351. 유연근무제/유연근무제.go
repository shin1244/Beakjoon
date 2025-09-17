func solution(schedules []int, timelogs [][]int, startday int) int {
	after10min := []int{}
	result := len(schedules)

	for _, schedule := range schedules {
		hour := schedule / 100
		min := schedule%100 + 10
		if min >= 60 {
			hour++
			min -= 60
		}
		after10min = append(after10min, hour*100+min)
	}

	for idx, times := range timelogs {
		standard := after10min[idx]
		for dayIdx, time := range times {
			if standard < time && (dayIdx+startday)%7 != 0 && (dayIdx+startday)%7 != 6 {
				result--
				break
			}
		}
	}

	return result
}
