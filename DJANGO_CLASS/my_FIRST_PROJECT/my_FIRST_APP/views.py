from django.shortcuts import render
from .models import Dea

# Create your views here.


def home(request):
    my_dea = Dea.objects.all()
    return render(request, "my_FIRST_APP/index.html", {"my_dea": my_dea})