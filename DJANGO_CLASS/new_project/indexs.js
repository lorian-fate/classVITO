fetch("http://localhost:8000/api/2021-114")
.then((res) => res.json())
.then((data) => {
    const dea = data[0];
    const via_nombre = document.querySelector("#via_nombre")
    via_nombre.innerText = dea.direccion_via_nombre;
})