package main

import (
	"log"
	"net/http"
)

// Обработчик главной страницы
func home(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/" {
		http.NotFound(w, r)
		log.Println("Пошли на несуществующую страницу")
		return
	}
	w.Write([]byte("Привет это главная страница"))
	log.Println("Перешли на Home")
}

// Обработчик страницы Об
func about(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Ну а эта страница о нашем сайте"))
	log.Println("Вернулись на about")
}

func main() {
	// Регистрируем обработчики
	mux := http.NewServeMux()
	mux.HandleFunc("/", home)
	mux.HandleFunc("/about", about)

	log.Print("Запуск веб-сервера на http://127.0.0.1:4000")
	err := http.ListenAndServe(":4000", mux)
	log.Fatal(err)
}
