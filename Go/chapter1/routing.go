package main

import (
	// "debug/elf"
	"encoding/json"
	// "fmt"
	"html/template"
	"log"
	"net/http"
	"strconv"
)

// Тип пользователь
type User struct {
	Name      string `json:"name"`
	Last_name string `json:"last_name"`
	City      string `json:"city"`
	Born      string `json:"born"`
}

// Обработчик главной страницы
func root_page(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/" {
		http.NotFound(w, r)
		log.Println("Пошли на несуществующую страницу")
		return
	}
	tmpl, _ := template.ParseFiles("html_templates/home_page.html")
	tmpl.Execute(w, nil)
	log.Println("Перешли на Home")
}

func home_page(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/home" {
		http.NotFound(w, r)
		log.Println("Пошли на несуществующую страницу")
		return
	}
	tmpl, _ := template.ParseFiles("html_templates/home_page.html")
	tmpl.Execute(w, nil)
	log.Println("Перешли на Home")
}

// Обработчик страницы Об
func about_page(w http.ResponseWriter, r *http.Request) {

	user := User{
		Name:      "Dima",
		Last_name: "Zhuravlev",
		City:      "Krasnodar",
		Born:      "30-12-1996",
	}

	//Сериализуем структуру в строку
	jsonString, _ := json.Marshal(&user)

	w.Write(jsonString)
	log.Println("Вернулись на about")

}

func showSomeId(w http.ResponseWriter, r *http.Request) {
	id1, _ := strconv.Atoi(r.URL.Query().Get("id1"))
	id2, _ := strconv.Atoi(r.URL.Query().Get("id2"))

	type ViewData struct {
		Id1 string
		Id2 string
	}

	data := ViewData{
		Id1: strconv.Itoa(id1),
		Id2: strconv.Itoa(id2),
	}

	tmpl, _ := template.ParseFiles("html_templates/showSameId.html")
	tmpl.Execute(w, data)

}
func selectPage(w http.ResponseWriter, r *http.Request) {
	page, _ := strconv.Atoi(r.URL.Query().Get("page"))
	// fmt.Fprintf(w, "hsdgfhd %s", page)
	if page == 1 {
		tmpl, _ := template.ParseFiles("html_templates/1.html")
		tmpl.Execute(w, nil)
	} else if page == 2 {
		tmpl, _ := template.ParseFiles("html_templates/2.html")
		tmpl.Execute(w, nil)
	} else {
		tmpl, _ := template.ParseFiles("html_templates/3.html")
		tmpl.Execute(w, nil)
	}
}

func main() {
	// Регистрируем обработчики
	mux := http.NewServeMux()
	mux.HandleFunc("/", root_page)
	mux.HandleFunc("/home", home_page)
	mux.HandleFunc("/about", about_page)
	mux.HandleFunc("/show", showSomeId)
	mux.HandleFunc("/select", selectPage)

	log.Print("Запуск веб-сервера на http://127.0.0.1:4000")
	err := http.ListenAndServe(":4000", mux)
	log.Fatal(err)
}
