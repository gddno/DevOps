package main

import (
	"strings"
	"fmt"
)

func main(){
	fmt.Println("Вы хотите выйти из перещеры?")

	var command = "выйти наружу"
	var exit = strings.Contains(command, "наружу")

	fmt.Println("Вы покидаете пещеру:", exit)

	var sunny = "светит яркое солнце"
	var takeOn = strings.Contains(sunny, "яркое солнце")

	var inscription = "Прочти пособие по БЖД"
	var verification = strings.Contains(inscription, "Прочти")

	fmt.Println("Вы покидаете пещеру:", exit)
	fmt.Println("Вы надеваете очки:", takeOn)
	fmt.Println("Содержит ли 'Прочти':", verification)
}