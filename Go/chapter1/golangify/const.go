package main

import (
	"fmt"
	// "math/big"
)


func main(){
	const a = 236000000000000000
	const secPerDay = 86400
	const speedLight = 299792
	const dayInYear = 365

	const years = a / speedLight /secPerDay /dayInYear

	fmt.Println("Растояние то", years, "года!!!")
}

