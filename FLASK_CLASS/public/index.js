//alert("we are here again")

fetch("http://localhost:3000/api/all")
    .then((res) => res.json())
    .then((data) => {
        data = data["data"]
        console.log(data)
        const ul = document.querySelector("#aqui")

        for (dea of data){
            const li = document.createElement("li")
            li.innerText = dea.direccion_via_nombre
            ul.append(li)
        }
    })