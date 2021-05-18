from django.shortcuts import render
from .models import Dea
from .get_DEA import get_distance

# Create your views here.

"""
def home(request):
    my_dea = Dea.objects.all()
    return render(request, "my_FIRST_APP/index.html", {"my_dea": my_dea})
"""
    

#def closest_DEA(request):
def home(request):
    #my_ubication = ()
    more_D = Dea.objects.all()
    #print(get_distance(more_D)[3])
    #print(more_D[0].codigo_dea)

    dea_code = get_distance(more_D)[3]
    dea_code = dea_code.codigo_dea
    #dea_and_user_position = [get_distance(more_D)[0], get_distance(more_D)[1]]

    my_dea = Dea.objects.filter(codigo_dea=dea_code)
    return render(request, "my_FIRST_APP/index.html", {"my_dea": my_dea})


def my_map(request):
    more_D = Dea.objects.all()
    dea_pos = get_distance(more_D)[0]
    user_pos = get_distance(more_D)[1]

    my_url  = f"https://www.google.com/maps/dir/{user_pos[0]},+{user_pos[1]}/{dea_pos[0]},{dea_pos[1]}"
    return render(request, my_url)



def user_ubication(request):
    if request.method == "POST":
        print(request.POST)
        lat_long = [float(request.POST['lat']), float(request.POST['long'])] 
    return render(request, "my_FIRST_APP/user_position.html")

