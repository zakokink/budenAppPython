from django.shortcuts import render,HttpResponse
from .models import Training
def home(request):
    return render(request, "home.html")

def alleTrainings(request):
    trainings = Training.objects.all()
    return render(request, "alleTrainings.html", {"trainings": trainings})



