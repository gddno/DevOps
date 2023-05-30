package main

import(
	"fmt"
	"math/rand"
)

const SecPerDay = 86400

func main(){
	company := ""
	distance := 64100000
	tour := ""

	fmt.Println("============================================")
	fmt.Println("Spaceline         Days    Trip type    Price")
	fmt.Println("============================================")
	for count := 10; count > 0; count--{
	if rand.Intn(2) == 1 {
	tour = "One-way"
	}else {
		tour = "Round-trip"
	}
	speed := rand.Intn(15) + 16

	duration := distance / speed / SecPerDay

	price := 20.0 + speed

	switch rand.Intn(3){
	case 1: company = "Virgin Galactic"
	case 2: company = "Space X"
	case 3: company = "Space Adventure" 
	}

	fmt.Printf("|%-17v|%-7v|%-11v|$%3v|\n", company, duration, tour, price)
	
}
		
}
