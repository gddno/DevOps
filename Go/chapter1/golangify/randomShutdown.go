package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main(){
	var startCount = 10
	
	for startCount > 0 {
		fmt.Println(startCount)

		time.Sleep(time.Second)
			if rand.Intn(10) == 0 {
				break
			}
		startCount--
		}
		if startCount == 0 {
			fmt.Println("Start!!!")
		} else {
			fmt.Println("Start will not!!!")
		}
	}
