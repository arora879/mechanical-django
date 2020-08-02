from django.shortcuts import render
from django.http import HttpResponse
from .models import Services


def index(request):
    mydict = {'services' : Services.objects.all()}
    print(mydict)
    return render(request, "index.html", context=mydict)