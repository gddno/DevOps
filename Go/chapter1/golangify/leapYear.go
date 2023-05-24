package main

import (
	"fmt"
	// "math/rand"
	// "go/constant"
)

func main() {
	year := 2038//rand.Intn(2050 - 2000 ) + 2000
	var leap = year%400 == 0 || (year%100 != 0 && year%4 == 0)
	if leap {
		fmt.Printf("%v год високосный", year)
	} else {
		fmt.Printf("%v к сожалению не високосный", year)
	}
}