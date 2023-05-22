package main

import (
	"fmt"
	"time"
)

func main(){
	switch time.Now().Weekday(){
	case time.Monday:
		fmt.Println("Today Monday")
	case time.Tuesday:
		fmt.Println("Today Tuesday")
	case time.Wednesday:
		fmt.Println("Today Wednesday")
	case time.Thursday:
		fmt.Println("Today Thursday")
	case time.Friday:
		fmt.Println("Today Friday")
	case time.Saturday:
		fmt.Println("Today Saturday")
	case time.Sunday:
		fmt.Println("Today Sunday")
	}
	switch time.Now().Weekday(){
	case time.Monday, time.Tuesday, time.Wednesday, time.Thursday, time.Friday:
		fmt.Println("И да он будний день")
	case time.Saturday, time.Sunday:
		fmt.Println("И да он выходной")
	}

}
