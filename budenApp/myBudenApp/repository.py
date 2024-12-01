from django.shortcuts import render,HttpResponse
from .models import Training, Uebungen, User
from django.db.models import Max

def getLatestTrainingForUebungAndUser(userId, uebungId):
    maxDate = Training.objects.filter(uebung = uebungId, user = userId).aggregate(Max('date'))['date__max']
    if(maxDate == None):
        return None

    trainingWithMaxForUebung = Training.objects.filter(date = str(maxDate), uebung = uebungId, user = userId)

    return trainingWithMaxForUebung


def getLatestGewichtForUebungAndUser(userId, uebungId):
    maxDate = Training.objects.filter(uebung = uebungId, user = userId).aggregate(Max('date'))['date__max']
    if(maxDate == None):
        return None

    trainingWithMaxForUebung = Training.objects.filter(date = str(maxDate), uebung = uebungId, user = userId)

    return trainingWithMaxForUebung[0].gewicht

def getUebungen():
    uebungen = Uebungen.objects.all()
    return uebungen