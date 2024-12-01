from django.shortcuts import render,HttpResponse
from .models import Training, Uebungen, User
from django.db.models import Max

def getLatestTrainingForUebungAndUser(userId, uebungId):
    #uebid = Uebungen.objects.get(uebung='Beinpresse')
    #userid = User.objects.get(name='Salomon')

    maxDate = Training.objects.filter(uebung = uebungId, user = userId).aggregate(Max('date'))['date__max']
    if(maxDate == None):
        return None

    trainingWithMaxForUebung = Training.objects.filter(date = str(maxDate), uebung = uebungId, user = userId)

    return trainingWithMaxForUebung


def getLatestGewichtForUebungAndUser(userId, uebungId):
    #uebid = Uebungen.objects.get(uebung='Beinpresse')
    #userid = User.objects.get(name='Salomon')

    maxDate = Training.objects.filter(uebung = uebungId, user = userId).aggregate(Max('date'))['date__max']
    if(maxDate == None):
        return None

    trainingWithMaxForUebung = Training.objects.filter(date = str(maxDate), uebung = uebungId, user = userId)

    return trainingWithMaxForUebung[0].gewicht

def getUebungen():
    uebungen = Uebungen.objects.all()
    return uebungen