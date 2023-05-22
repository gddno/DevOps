package main

import "fmt"

func main (){
	var room = "озеро"

	switch{
	case room == "пещера":
		fmt.Println("Вы в пещере")
	case room == "озеро":
		fmt.Println("Эх Рица")
		fallthrough
	case room == "глубина":
		fmt.Println("Озеро Рица очень глубокое")
	}
}