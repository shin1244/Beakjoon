import (
	"sort"
)

func solution(k int, tangerine []int) int {
	result := 0
	countMap := make(map[int]int)
	for _, val := range tangerine {
		countMap[val]++
	}
	sort.Slice(tangerine, func(i, j int) bool {
		if countMap[tangerine[i]] == countMap[tangerine[j]] {
			return tangerine[i] < tangerine[j]
		}
		return countMap[tangerine[i]] < countMap[tangerine[j]]
	})

	countMap = make(map[int]int)
	for _, val := range tangerine[len(tangerine)-k:] {
		countMap[val]++
	}
	for range countMap {
		result++
	}
	return result
}