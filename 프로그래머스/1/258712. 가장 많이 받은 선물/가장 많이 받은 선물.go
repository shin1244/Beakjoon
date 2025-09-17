import (
    "strings"
)

func solution(friends []string, gifts []string) int {
	resultMap := make(map[string]int)
	score := make(map[string]int)
	giftHistory := make(map[string]map[string]int)

	for _, friend := range friends {
		giftHistory[friend] = make(map[string]int)
	}

	for _, gift := range gifts {
		giveNtake := strings.Split(gift, " ")
		giver, taker := giveNtake[0], giveNtake[1]
		giftHistory[giver][taker]++
		score[giver]++
		score[taker]--
	}

	for i := 0; i < len(friends); i++ {
		for j := i + 1; j < len(friends); j++ {
			a, b := friends[i], friends[j]

			if giftHistory[a][b] > giftHistory[b][a] {
				resultMap[a]++
			} else if giftHistory[a][b] < giftHistory[b][a] {
				resultMap[b]++
			} else {
				if score[a] > score[b] {
					resultMap[a]++
				} else if score[a] < score[b] {
					resultMap[b]++
				}
			}
		}
	}

	result := 0
	for _, v := range resultMap {
		if v > result {
			result = v
		}
	}

	return result
}

