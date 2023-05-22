package main

import (
	"fmt"

)

func main(){

	var data interface {}
	data = true 
	switch mytype := data.(type){
	case bool:
		fmt.Println("This is bool")
	case string:
		fmt.Println("This is string")
	default:
		fmt.Println("%T", mytype)
	}
}