package main

import (
	"fmt"
)

func main(){
	size := "d"
	
	switch size {
	case "XXS":
		fmt.Println("So little")
	case "XXXL":
		fmt.Println("So BIG")
	default:
		fmt.Println("Size not was setting")
	}
}