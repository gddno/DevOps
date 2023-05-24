package main


import (
	"fmt"
	"math/rand"
)
var era = "AD"
func main(){
	for count := 10; count > 0; count --{
	var daysInMonth = 31
	yaer := rand.Intn(2050-2000)+2000
	month := rand.Intn(12) + 1
	leap := yaer%400 == 0 || (yaer%100 == 0 && yaer%4 == 0) 
		
	switch month{
	case 2:
		daysInMonth = 28
		if leap{
			daysInMonth = 29
		}
	case 4, 6, 9, 11:
		daysInMonth = 30
	//day := rand.Intn(daysInMonth) + 1 
	
	}
	fmt.Println(era,yaer, month, daysInMonth)
	} 
	
}