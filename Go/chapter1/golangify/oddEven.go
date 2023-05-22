package main


import (
	"fmt"
)

func main(){
	switch num := 9; num % 2 == 0{
	case true:
		fmt.Println("value even")
	case false:
		fmt.Println("value odd")
	}
	
}