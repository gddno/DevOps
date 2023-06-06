package main

import (
	"fmt"
	//"strconv"
	// "math"
	//"strconv"
)

func main() {
	// new := uint8(red)
	// fmt.Printf("%v", new)

	// age := 27
	// marsDays := 687
	// earthDays := 365.2425
	// fmt.Println("I am", age*earthDays/marsDays, "years old on Mars!!!")

	// var bh float64 = 32767
	// var h = int16(bh)
	// fmt.Println(h)

	// 	v := 33726
	// 	if v >= 0 && v < math.MaxInt8 {
	// 		v8 := uint8(v)
	// 	fmt.Println("converted:", v8)
	// }

	// countdown := 10
	// fmt.Println("This " + strconv.Itoa(countdown) + " value")
	// fmt.Sprintf("This is %v dollars $", countdown)

	// launch := false
	// launchText := fmt.Sprintf("%v", launch)
	// fmt.Println("Ready for launch:", launchText)

	// var yesNo string
	// if launch {
	// 	yesNo = "yes"
	// } else {
	// 	yesNo = "no"
	// }
	// fmt.Println("Ready for launch:", yesNo)

	// yesNo := "no"

	// launch := (yesNo == "yes")
	// fmt.Println("Ready for launch:", launch)

	// launch := true
	// var oneZero int
	// if launch{
	// 	oneZero = 1
	// } else {
	// 	oneZero = 0
	// }
	// fmt.Println("Ready for launch:", oneZero)

	yesNo := "0"
	var launch bool
	switch yesNo {
	case "1", "yes", "true":
		launch = true
	case "0", "no", "false":
		launch = false
	default:
		fmt.Println(yesNo, "is not valid")
	}
	fmt.Println("Ready for launch:", launch)
}
