package main

import "fmt"

func main(){
	fmt.Println("Вы находитесь в стартовом локации")
	var action = "Идем в пывыоход"
	
	switch action{
	case "Стоим на месте":
		fmt.Println("Вы остались на том же месте")
	case "Идем в поход":
		fmt.Println("Ура вы идете вперед и развиваетесь!!!")
	case "Куда выведет":
		fmt.Println("Вы полагаетесь на волю судьбы!!!")
	default:
		fmt.Println("Пока не очень ясно куда вы держите свой путь")
	}

}