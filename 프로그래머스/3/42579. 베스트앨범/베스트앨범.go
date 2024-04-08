import (
	"sort"
)

func solution(genres []string, plays []int) []int {
	dict := make(map[string][][]int)
	arr := [][][]int{}
	result := []int{}

	for idx, genre := range genres {
		dict[genre] = append(dict[genre], []int{plays[idx], idx})
	}

	for _, value := range dict {
		sort.Slice(value, func(i, j int) bool {
			if value[i][0] == value[j][0] {
				return value[i][1] < value[j][1]
			}
			return value[i][0] > value[j][0]
		})
		arr = append(arr, value)
	}

	sort.Slice(arr, func(i, j int) bool {
		sumI, sumJ := 0, 0
		for _, val := range arr[i] {
			sumI += val[0]
		}
		for _, val := range arr[j] {
			sumJ += val[0]
		}
		return sumI > sumJ
	})

	for i := 0; i < len(arr); i++ {
		result = append(result, arr[i][0][1])
		if len(arr[i]) >= 2 {
			result = append(result, arr[i][1][1])
		}
	}

	return result
}