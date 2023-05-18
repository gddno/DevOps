package main

import (
	"encoding/json"
	"html/template"
	"log"
	"net/http"
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
	// w.Write([]byte("Привет это главная страница"))
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
	// w.Write([]byte("Привет это главная страница"))
	log.Println("Перешли на Home")
}

// Обработчик страницы Об
func about_page(w http.ResponseWriter, r *http.Request) {
	// w.Write([]byte("Ну а эта страница о нашем сайте"))
	user := User{
		Name:      "Dima",
		Last_name: "Zhuravlev",
		City:      "Krasnodar",
		Born:      "30-12-1996",
	}

	//Сериализуем структуру в строку
	jsonString, _ := json.Marshal(&user)
	// if err != nil {
	// 	log.Fatalln("marshal ", err.Error())
	// }
	// w.Write([]byte(dima))
	w.Write(jsonString)
	log.Println("Вернулись на about")

	// deserializeJson, err := User{}
	// err = json.Unmarshal([]byte(jsonString), &deserializeJson)
	// if err != nil {
	// 	log.Fatalln("unmarshal ", err.Error())
	// }

	// w.Write([]byte(deserializeJson))

}

func main() {
	// Регистрируем обработчики
	mux := http.NewServeMux()
	mux.HandleFunc("/", root_page)
	mux.HandleFunc("/home", home_page)
	mux.HandleFunc("/about", about_page)

	log.Print("Запуск веб-сервера на http://127.0.0.1:4000")
	err := http.ListenAndServe(":4000", mux)
	log.Fatal(err)
}
