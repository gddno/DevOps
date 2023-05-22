package main

import (
	"fmt"
	"math/rand"
)

func main(){
	var myCount = 15
	var countCheck = 0
	for {
		countCheck ++
		var computerCount = rand.Intn(30 - 0 + 1) - 0
		if computerCount > myCount{
			fmt.Printf("Число компьбтера больше тавоего!!!%v\n", countCheck)
		} else if computerCount < myCount{
			fmt.Printf("Число компьютера менше твоего!!!%v\n", countCheck)
		} else {
			fmt.Printf("Угадалллл!!!%v\n", countCheck)
			break
		}

	}
	
}