package main

import (
	"encoding/json"
	"fmt"
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
//Меняем html шаблон из строки браузера
func showSomeId(w http.ResponseWriter, r *http.Request) {
	id1, _ := strconv.Atoi(r.URL.Query().Get("id1"))
	id2, _ := strconv.Atoi(r.URL.Query().Get("id2"))
	id3, _ := strconv.Atoi(r.URL.Query().Get("id3"))

	type ViewData struct {
		Id1 string
		Id2 string
		Id3 string
	};

	data := ViewData{
		Id1: strconv.Itoa(id1),
		Id2: strconv.Itoa(id2),
		Id3: strconv.Itoa(id3),
	}

	tmpl, _ := template.ParseFiles("html_templates/showSameId.html")
	tmpl.Execute(w, data)
	log.Println("Изменили HTML страницу")

}
// Открытие определенной html страницы из браузера
func selectPage(w http.ResponseWriter, r *http.Request) {
	page, _ := strconv.Atoi(r.URL.Query().Get("page"))
	// Sprintf позволяет положить в переменную значение из строки браузера
	var text = fmt.Sprintf("html_templates/%v.html", page)
	
	// Выыодим страницу из папки html_template и в случае ошибки выводим КУЛЬТУРНО, что страница не найдена 
	tmpl, err := template.ParseFiles(text)
		if err != nil{
			// http.NotFound(w, r)
			tmpl, _ := template.ParseFiles("html_templates/ErrorMessage.html")
			tmpl.Execute(w, nil)
			log.Println("Пошли на несуществующую страницу")
		return
		}
		
	tmpl.Execute(w,nil)
	log.Println("Вывели нужную нам страницу")
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
