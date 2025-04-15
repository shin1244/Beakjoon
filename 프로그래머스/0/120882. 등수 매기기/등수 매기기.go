import "sort"

func solution(score [][]int) []int {
    avgScores := []int{}
    for _, val := range score {
        avgScores = append(avgScores,val[0] + val[1])
    }
    
    sortedScores := make([]int, len(avgScores))
    copy(sortedScores, avgScores)
    sort.Slice(sortedScores, func(i, j int) bool {
        return sortedScores[i] > sortedScores[j]
    })
    
    result := []int{}
    for _, avgVal := range avgScores {
        for idx, sortVal := range sortedScores {
            if avgVal == sortVal {
                result = append(result, idx + 1)
                break
            }
        }
    }
    
    return result
}