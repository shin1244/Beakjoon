package main

import (
	"fmt"
)

func main() {
	var len int
	fmt.Scan(&len)

	arr := [][]int{}

	DP := make([]int, len+1)

	for i := 0; i < len; i++ {
		var a, b int
		fmt.Scan(&a, &b)
		arr = append(arr, []int{a, b})
	}

	for i := 0; i < len; i++ {
		if i+arr[i][0] <= len {
			DP[i+arr[i][0]] = max(DP[i+arr[i][0]], DP[i]+arr[i][1])
		}
		DP[i+1] = max(DP[i+1], DP[i])
	}

	fmt.Println(DP[len])
}
