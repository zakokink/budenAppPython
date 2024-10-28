from django.shortcuts import render,HttpResponse
from .models import Training, Uebungen, User
from django.db.models import Max
from django.core import serializers

from .repository import getLatestTrainingForUebungAndUser, getLatestGewichtForUebungAndUser


def home(request):
    return render(request, "home.html")

def alleTrainings(request):
    uebid = Uebungen.objects.get(uebung='Beinpresse')
    userid = User.objects.get(name='Salomon')

    #print(userid)
    #print(uebid.id)
    #trainings = Training.objects.filter(uebung = uebid.id, user = 1, ).order_by('-date')[0]
    #trainingsArray = []
    #trainingsArray.append(trainings)

    #trainings2 = Training.objects.aggregate(Max('gewicht'))
    maxDate = Training.objects.filter(uebung = uebid.id, user = userid).aggregate(Max('date'))['date__max']
    trainingWithMaxForUebung = Training.objects.filter(date = str(maxDate), uebung = uebid.id, user = userid)

    #print(str(maxDate))


    #print('trainingWithMaxForUebung date: ')
    #print(trainingWithMaxForUebung)


    #trainings1 = Training.objects.filter(uebung=uebid.id).order_by('-date')[0]
    #print(trainings1.gewicht)

    #trainings = Training.objects.raw("select * from myBudenApp_training")

    #query = 'select * from myBudenApp_training where user.user=Salomon'

    #query = "select * from myBudenApp_training where date in (select max(date) from myBudenApp_training where uebung=2 having uebung=2)"

    #trainings = Training.objects.raw(query)

    #trainings = Training.objects.all()

    result1 = getLatestTrainingForUebungAndUser(userid,uebid)
    if(len(result1) > 0):
        print(result1[0])

    result2 = getLatestGewichtForUebungAndUser(userid,uebid)
    print(result2)

    return render(request, "alleTrainings.html", {"trainings": trainingWithMaxForUebung})

def alleTrainingsJson(request):
    result = Training.objects.all()
    data = serializers.serialize('json', result)
    print(data)

    return HttpResponse(data)








