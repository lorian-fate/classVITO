from django.shortcuts import render
from .models import Dea
from .get_DEA import get_distance
from django.core import serializers
from django.http.response import JsonResponse

# Create your views here.


def home(request):
    my_dea = Dea.objects.all()
    return render(request, "my_FIRST_APP/home.html", {"my_dea": my_dea})


def list_DEA(request):
    my_dea = Dea.objects.all()
    return render(request, "my_FIRST_APP/index.html", {"my_dea": my_dea})
    

def closest_DEA(request):
    more_D = Dea.objects.all()
    
    if request.method == "POST":
        lat = request.POST["lat"]
        lng = request.POST["long"]
        user_point = (float(lat), float(lng))
        print(user_point)
        dea_code = get_distance(more_D, user_point)

        my_dea = Dea.objects.filter(codigo_dea=dea_code[2].codigo_dea)
        dea_pos = dea_code[0]

        my_url  = f"https://www.google.com/maps/dir/{lat},+{lng}/{dea_pos[0]},{dea_pos[1]}"
        return render(request, "my_FIRST_APP/founded.html", {"my_dea": my_dea, "my_url":my_url})



def my_map(request):
    more_D = Dea.objects.all()
    dea_pos = get_distance(more_D)[0]
    user_pos = get_distance(more_D)[1]

    if request.method == "POST":
        lat = request.POST["lat"]
        long = request.POST["long"]
        my_url  = f"https://www.google.com/maps/dir/{user_pos[0]},+{user_pos[1]}/{dea_pos[0]},{dea_pos[1]}"
        return render(request, my_url)



def user_ubication(request):
    return render(request, "my_FIRST_APP/search.html")


def log_user(request):
    return render(request, "my_FIRST_APP/login.html")


def my_api(request):
    my_data = Dea.objects.all()
    print(type(my_data))
    my_json = [
        {"codigo_Dea": dea.codigo_dea,
        "direccion_ubicacion": dea.direccion_ubicacion,
        "direccion_portal_numero": dea.direccion_portal_numero,
        "horario_acceso": dea.horario_acceso,
        "x_utm": dea.x_utm,
        "y_utm": dea.y_utm
        } for dea in my_data
    ]
    return JsonResponse({"data":  my_json})

def solo_dea(request, codigo):
    my_dea = Dea.objects.filter(codigo_dea=codigo)
    if my_dea.count():
        print(my_dea.count())
        return JsonResponse({"dea": {
            "codigo_Dea": my_dea[0].codigo_dea,
            "direccion_ubicacion": my_dea[0].direccion_ubicacion,
            "direccion_portal_numero": my_dea[0].direccion_portal_numero,
            "horario_acceso": my_dea[0].horario_acceso,
            "x_utm": my_dea[0].x_utm,
            "y_utm": my_dea[0].y_utm
        }})
    else:
        return JsonResponse({"data": "non existent dea code"})
    