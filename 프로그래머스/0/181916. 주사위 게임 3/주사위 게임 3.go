import (
    "sort"
)

type dice struct {
    key int
    val int
}

func solution(a int, b int, c int, d int) int {
    dict := make(map[int]int)
    
    for _, val := range []int{a, b ,c, d} {
        dict[val]++
    }
    
    var diceSlice []dice
    for key, val := range dict {
        if val == 4 {
            return 1111 * key
        }
        diceSlice = append(diceSlice, dice{key, val})
    }
    sort.Slice(diceSlice, func(i, j int) bool {
        if diceSlice[i].val == diceSlice[j].val {
            return diceSlice[i].key < diceSlice[j].key
        }
        return diceSlice[i].val > diceSlice[j].val
    })
    if diceSlice[0].val == 1 {
        return diceSlice[0].key
    }
    
    arr := []int{}
    for _, dice := range diceSlice {
        arr = append(arr, dice.val)
    }
    if arr[0] == 3 {
        return (diceSlice[0].key * 10 + diceSlice[1].key) * (diceSlice[0].key * 10 + diceSlice[1].key)
    } else if arr[1] == 2 {
        return (diceSlice[0].key + diceSlice[1].key) * (diceSlice[1].key - diceSlice[0].key)
    }
    return diceSlice[1].key * diceSlice[2].key
}