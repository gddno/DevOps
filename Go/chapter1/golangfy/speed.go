package main

import (
	"fmt"
	//"math/rand"
)

func main() {
	const srok = 28
	const DayPer = 24
	var distance = 56000000

	//fmt.Println(distance/speed, "дней")

	// distance = 40100000
	// fmt.Println(distance/speed/24, "секунд")

	// var hoursPerDay, minutesPerHour = 24, 60

	//var weight -= 2

	//var num = rand.Intn(4 - 1) + 1
	fmt.Println(distance/(srok*DayPer), "km/h")
}
