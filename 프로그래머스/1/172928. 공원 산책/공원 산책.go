import (
	"strconv"
	"strings"
)

func solution(park []string, routes []string) []int {
	nowY := -1
	nowX := -1
	YLen := len(park)
	XLen := len(park[0])
	for yIdx := range park {
		for xIdx := range park[yIdx] {
			if park[yIdx][xIdx] == 'S' {
				nowX = xIdx
				nowY = yIdx
			}
		}
	}

	for _, route := range routes {
		r := strings.Split(route, " ")
		direction := r[0]
		distance, _ := strconv.Atoi(r[1])
		check := true

		switch direction {
		case "N":
			if nowY-distance >= 0 {
				for i := nowY; i >= nowY-distance; i-- {
					if park[i][nowX] == 'X' {
						check = false
						break
					}
				}
				if check {
					nowY = nowY - distance
				}
			}
		case "S":
			if nowY+distance < YLen {
				for i := nowY; i <= nowY+distance; i++ {
					if park[i][nowX] == 'X' {
						check = false
						break
					}
				}
				if check {
					nowY = nowY + distance
				}
			}
		case "W":
			if nowX-distance >= 0 {
				for i := nowX; i >= nowX-distance; i-- {
					if park[nowY][i] == 'X' {
						check = false
						break
					}
				}
				if check {
					nowX = nowX - distance
				}
			}
		case "E":
			if nowX+distance < XLen {
				for i := nowX; i <= nowX+distance; i++ {
					if park[nowY][i] == 'X' {
						check = false
						break
					}
				}
				if check {
					nowX = nowX + distance
				}
			}
		}
	}

	return []int{nowY, nowX}
}
