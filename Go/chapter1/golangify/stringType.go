package main

import (
	"fmt"
)

func main(){
	// var star byte = '*'
	// smile := ''
	// acute := 'e'
	
	// fmt.Printf("%c %[1]v\n", star)
	// fmt.Printf("%c %[1]v\n", smile)
	// fmt.Printf("%c %[1]v\n", acute)


	var star byte = '*'
	fmt.Printf("%c %[1]v\n", star) // Выводит: * 42
 
	smile := ''
	fmt.Printf("%c %[1]v\n", smile) // Выводит: ? 128515
 
	acute := 'é'
	fmt.Printf("%c %[1]v\n", acute) // Выводит: é 233
}