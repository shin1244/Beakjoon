func solution(players []string, callings []string) []string {
    rank := make(map[string]int)
    for idx, val := range players {
        rank[val] = idx 
    }
    
    for _, call := range callings {
        pr := rank[call]
        players[pr], players[pr-1] = players[pr-1], players[pr]
        rank[call], rank[players[pr]] = pr-1, pr
    }
    
    return players
}