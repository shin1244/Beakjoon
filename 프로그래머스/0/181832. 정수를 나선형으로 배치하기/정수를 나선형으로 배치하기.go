func solution(n int) [][]int {
    result := make([][]int, n)
    for i := range result {
        result[i] = make([]int, n)
    }
    
    dy := []int{0, 1, 0, -1}
    dx := []int{1, 0, -1, 0}
    
    x, y, num, dir := 0, 0, 1, 0
    
    for num <= n*n {
        result[y][x] = num
        num++
        
        ny, nx := y+dy[dir], x+dx[dir]
        if ny < 0 || nx < 0 || ny >=n || nx >= n || result[ny][nx] != 0 {
            dir = (dir+1)%4
            ny, nx = y+dy[dir], x+dx[dir]
        }
        x, y = nx, ny
    }
    return result
}