package main

import (
	"fmt"
)

func main(){
	w := "a  b c\td\nefg hi"
	for _, e := range w{
		switch e {
		case ' ', '\n', '\t':
			break
		default:
			fmt.Printf("%c\n", e)
		}
	}
}