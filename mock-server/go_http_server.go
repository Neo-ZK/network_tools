package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"strings"
    "time"
)

type AutotaskRequest struct {
	RequestID string `json:"identity"`
}

func sayhelloName(w http.ResponseWriter, r *http.Request) {
	body, _ := ioutil.ReadAll(r.Body) //把  body 内容读入字符串 s
	fmt.Println(body)
	r.ParseForm()       // 解析参数，默认是不会解析的
	fmt.Println(r.Form) // 这些信息是输出到服务器端的打印信息
	fmt.Println("path", r.URL.Path)
	fmt.Println("scheme", r.URL.Scheme)
	fmt.Println(r.Form["url_long"])
    fmt.Fprintf(w, "first output") // 这个写入>到 w 的是输出到客户端的
    time.Sleep(time.Duration(10)*time.Second)
	for k, v := range r.Form {
		fmt.Println("key:", k)
		fmt.Println("val:", strings.Join(v, ""))
	}
	fmt.Fprintf(w, "second output") // 这个写入到 w 的是输出到客户端的
	var a AutotaskRequest
	if err := json.Unmarshal(body, &a); err != nil {
		fmt.Printf("Unmarshal err, %v\n", err)
		return
	}
	fmt.Println(a)
}

func main() {
	http.HandleFunc("/", sayhelloName)       // 设置访问的路由
	err := http.ListenAndServe(":8888", nil) // 设置监听的端口
	if err != nil {
		log.Fatal("ListenAndServe: ", err)
	}
}

