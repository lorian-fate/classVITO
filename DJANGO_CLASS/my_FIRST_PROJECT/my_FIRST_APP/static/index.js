


window.navigator.geolocation.getCurrentPosition((position) => {
    const lat = position.coords.latitude
    const long = position.coords.longitude
    console.log(lat, long)

    const input_lat = document.querySelector("#lat")
    const input_long = document.querySelector("#long")
    input_lat.value = lat
    input_long.value = long
})

