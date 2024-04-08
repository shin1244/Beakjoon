func solution(priorities []int, location int) int {
	result := 0
	arr := make([][]int, len(priorities))
	for i, val := range priorities {
		if i == location {
			arr[i] = []int{val, 1}
			continue
		}
		arr[i] = []int{val, 0}
	}

	for len(arr) > 0 {
		now := arr[0]
		arr = arr[1:]
		check := false
		for _, val := range arr {
			if now[0] < val[0] {
				check = true
				break
			}
		}
		if check {
			arr = append(arr, now)
			continue
		}
		result++
		if now[1] == 1 {
			return result
		}
	}
	return -1
}