package main

import (
	"fmt"
	//"unicode/utf8"
)

func main() {
	// peace := "peace"
	// var a = "peace"
	// var c string = "peace"
	// var blank string
	// fmt.Printf("%v, %v, %v, %v\n",peace, a, c, blank)
	// fmt.Println("Hello \nand baey!!!")
	// fmt.Println(`Hello
	// \n and
	// baey!!!`)
	// fmt.Printf("%v is a %[1]T\n", "literal string")
	// fmt.Printf("%v is a %[1]T\n", `raw string literal`)

	// var pi rune = 960
	// var omega rune = 969
	// var alpha rune = 940
	// var bang byte = 33

	// fmt.Printf("%c %c %c %c\n", pi, omega, alpha, bang)

	// 	grade := 'A'
	// 	var c = 'A'
	// 	var b rune = 'A'

	// 	fmt.Printf("%v %v %v", grade, c, b)
	//
	// star := '*'
	// fmt.Printf("%v\n", star)
	// smile := '?'
	// fmt.Printf("%v\n", smile)
	// acute := 'é'
	// fmt.Printf("%v\n", acute)

	// message := "shalom"
	// for c := 0; c < 6; c++{
	// 	fmt.Printf("%v\n", message[c])
	// }

	// c := 'g'
	// c = c - 'a' + 'A'
	// fmt.Printf("%c\n", c)

	// message := "uv vagreangvbany fcnpr fgngvba"
	// for c := 0; c < len(message); c++{
	// 	i := message[c]
	// 	if i >= 'a' && i <= 'z'{
	// 		i = i + 13
	// 		if i > 'z'{
	// 			i = i - 26
	// 		}
	// 	}
	// 	fmt.Printf("%c", i)
	// }

	// question := "¿Cómo estás?"
	// fmt.Println(len(question), "bytes")
	// fmt.Println(utf8.RuneCountInString(question), "runes")

	// c, size := utf8.DecodeRuneInString(question)
	// fmt.Printf("First rune: %c %v bytes", c, size)

	// message := "¿Cómo estás?"

	// for _, i := range message {
	// 	fmt.Printf("%c", i)
	// }

	// 	Eanglish := "abcdefghijklmnopqrstuvwxyz"
	// 	runa := "¿"
	// 		fmt.Println(len(runa), "bytes")
	// 		fmt.Println(utf8.RuneCountInString(Eanglish), "runes")
	// 		fmt.Println(len(Eanglish), "bytes")

	// 		message := "L fdph, L vdz, L frqtxhuhg"
	// 		for i := 0; i < len(message); i++ {
	// 			c := message[i]
	// 			if c >= 'a' && c <= 'z' {
	// 				c = c - 3
	// 				if c > 'z'{
	// 					c = c - 26
	// 				}
	// 			}
	// 			if c >= 'A' && c <='Z' {
	// 				c = c - 3
	// 				if c > 'Z'{
	// 					c = c - 26
	// 			}

	// 		}
	// 		fmt.Printf("%c", c)
	// }
	message := "Hola Estación Espacial Internacional"
	for _, c := range message {
		if c >= 'a' && c <= 'z' {
			c += 13
			if c > 'z' {
				c -= 26
			}
		} else if c >= 'A' && c <= 'Z' {
			c += 13
			if c > 'Z' {
				c -= 26
			}
		}
		fmt.Printf("%c", c)
	}
}
