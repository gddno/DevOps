package main

import "fmt"

func main(){
	var command = "Вышел из пещеры"

	if command == "Вышел из пещеры"{
		fmt.Println("Да ты вышел из своей пещеры и у тебя все получится!!!")
	} else if command != "Вышел из пещеры"{
		fmt.Println("Ты жалкая куча ГОВНА, так как не вышел из своей пещеры, но я верю в тебя, попробуй еще раз!!!")
	} else {
		fmt.Println("Ha-ha-ha")
	}
}