from django.shortcuts import render, HttpResponse, redirect
from .models import Dea
from .get_DEA import get_distance

# Create your views here.



def home(request):
    return render(request, "my_FIRST_APP/home.html")

def allDEA(request):
    my_dea = Dea.objects.all()
    return render(request, "my_FIRST_APP/index.html", {"my_dea": my_dea})


def closestDEA(request):
    #my_ubication = ()
    more_D = Dea.objects.all()
    #print(get_distance(more_D)[3])
    #print(more_D[0].codigo_dea)

    dea_code = get_distance(more_D)[3]
    dea_code = dea_code.codigo_dea
    #dea_and_user_position = [get_distance(more_D)[0], get_distance(more_D)[1]]

    my_dea = Dea.objects.filter(codigo_dea=dea_code)

    dea_pos = get_distance(more_D)[0]
    user_pos = get_distance(more_D)[1]

    my_url  = f"https://www.google.com/maps/dir/{user_pos[0]},+{user_pos[1]}/{dea_pos[0]},{dea_pos[1]}"


    return render(request, "my_FIRST_APP/index.html", {"my_dea": my_dea, "my_url": my_url})


def my_map(request):
    more_D = Dea.objects.all()
    dea_pos = get_distance(more_D)[0]
    user_pos = get_distance(more_D)[1]

    my_url  = f"https://www.google.com/maps/dir/{user_pos[0]},+{user_pos[1]}/{dea_pos[0]},{dea_pos[1]}"
    #return render(request, "my_FIRST_APP/index.html", my_url)
    return redirect(my_url)

#print(get_distance())

