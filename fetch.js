const arnaURL = "https://viacep.com.br/ws/79052420/json/"

fetch(arnaURL)
.then(res => {
    console.log("Status Resp:",res.status);
    console.log("Resposta:", res.ok);
    console.log("Endpoint Testado:", res.url)
    return res.json()
}).then(data => {
    console.log(data)
})
.catch(err => {
    console.error("Erro ->", err)
})



