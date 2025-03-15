package main

import (
    "fmt"
    "unicode"
)

func main() {
    var s1 string
    fmt.Scan(&s1)
    runes := []rune(s1)
    
    for idx, r := range runes {
        if unicode.IsUpper(r) {
            runes[idx] = unicode.ToLower(r)
        } else {
            runes[idx] = unicode.ToUpper(r)
        }
    }
    
    fmt.Println(string(runes))
}