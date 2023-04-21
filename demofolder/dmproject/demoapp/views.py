from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Team,Teamates


# Create your views here

def demo(request):
    obj = Place.objects.all()
    obj1 = Team.objects.all()
    obj2 = Teamates.objects.all()

    return render(request, "index.html", {'result': obj,'mates': obj1})



