import (
    "math/big"
)

func solution(a string, b string) string {
    intA := new(big.Int)
    intB := new(big.Int)
    intA.SetString(a, 10) 
    intB.SetString(b, 10)

    result := new(big.Int).Add(intA, intB) 
    return result.String() 
}
