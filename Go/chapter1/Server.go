package main

import (
	"fmt"
	"log"
	"net/http"
	"strings"
)

func HomeRouterHandler(w http.ResponseWriter, r *http.Request) {
	log.Default()

	r.ParseForm()
	fmt.Println(r.Form)
	fmt.Println("path", r.URL.Path)
	fmt.Println("scheme", r.URL.Scheme)
	fmt.Println(r.Form["url_long"])
	for k, v := range r.Form {
		fmt.Println("key:", k)
		fmt.Println("val:", strings.Join(v, ""))
	}
	fmt.Fprint(w, "Hello Dima")
}

func main() {
	http.HandleFunc("/", HomeRouterHandler)
	//err := http.ListenAndServe(":9000", nil)
	// if err != nil {
	log.Fatal(http.ListenAndServe(":9000", nil))
	// }
}
