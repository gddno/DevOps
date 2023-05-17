package main

import (
	"encoding/json"
	"html/template"
	"log"
	"net/http"
)
// Тип пользователь
type User struct{
	Name string
	Last_name string
	City string
	Born string
}

// Обработчик главной страницы
func home_page(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/" {
		http.NotFound(w, r)
		log.Println("Пошли на несуществующую страницу")
		return
	}
	tmpl, _ := template.ParseFiles("html_templates/home_page.html")
	tmpl.Execute(w, nil)
	// w.Write([]byte("Привет это главная страница"))
	log.Println("Перешли на Home")
}

// Обработчик страницы Об
func about_page(w http.ResponseWriter, r *http.Request) {
	// w.Write([]byte("Ну а эта страница о нашем сайте"))
	var dima User
    err := json.Unmarshal([]byte("/json_template/dima.json"), &dima)

    if err != nil {
        fmt.Println("JSON decode error!")
        return
    }
	w.Write([]byte(dima))
	log.Println("Вернулись на about")
}

func main() {
	// Регистрируем обработчики
	mux := http.NewServeMux()
	mux.HandleFunc("/", home_page)
	mux.HandleFunc("/about", about_page)

	log.Print("Запуск веб-сервера на http://127.0.0.1:4000")
	err := http.ListenAndServe(":4000", mux)
	log.Fatal(err)
}
