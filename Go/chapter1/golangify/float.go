package main


import (
	"fmt"
)

func main(){
	third := 10.0 / 3

	fmt.Println(third)
	fmt.Printf("%v\n", third)
	fmt.Printf("%f\n", third)
	fmt.Printf("%.3f\n", third)
	fmt.Printf("%03.8f\n", third)
}