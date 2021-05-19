


window.navigator.geolocation.getCurrentPosition((position) => {
    const lat = position.coords.latitude
    const long = position.coords.longitude
    console.log(lat, long)

    const input_long = document.querySelector("#long")
    
    const input_lat = document.querySelector("#lat")
    input_long.value = long
    input_lat.value = lat
    console.log(input_lat.value)
})

