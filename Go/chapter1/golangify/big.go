package main

import (
	"fmt"
	"math/big"
)



func main(){
	LightSpeed := big.NewInt(299792)
	SecondPerDay :=big.NewInt(86400)
	
	distance := new(big.Int)
	distance.SetString("24000000000000000000", 10)
	fmt.Println("Расстояние до галактики Андромеды составляет", distance, "км.")

	// a := new(big.Int)
	// a.SetString("24000000000000000000000", 10)

	f := big.NewInt(864000)


	c := big.NewInt(86400)

	v := new(big.Int)
	v.SetString("240000000000000000000", 10)


	seconds := new(big.Int)
	seconds.Div(distance, LightSpeed)
	
	days := new(big.Int)
	days.Div(seconds, SecondPerDay)

	fmt.Println("На это понадобится", days, "дня, если лететь со скоростью света!!!")
	fmt.Println(f)

}