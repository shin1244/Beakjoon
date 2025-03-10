func solution(n int, slicer []int, num_list []int) []int {
    result := []int{}
    switch n {
        case 1:
        return num_list[:slicer[1]+1]
        case 2:
        return num_list[slicer[0]:]
        case 3: 
        return num_list[slicer[0]:slicer[1]+1]
        case 4:
        for i := slicer[0]; i <= slicer[1]; i+=slicer[2] {
            result = append(result, num_list[i])
        }
    }
    return result
}