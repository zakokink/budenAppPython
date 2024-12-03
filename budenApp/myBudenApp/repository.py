from django.shortcuts import render,HttpResponse
from .models import Training, Uebungen, User, AktuelleLeistung
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

def getLatestGewichtAndWiederholungenForUebungAndUser(userId, uebungId):
    maxDate = Training.objects.filter(uebung = uebungId, user = userId).aggregate(Max('date'))['date__max']
    if(maxDate == None):
        return None

    trainingWithMaxForUebung = Training.objects.filter(date = str(maxDate), uebung = uebungId, user = userId)

    aktuelleLeistung = AktuelleLeistung()
    aktuelleLeistung.gewicht = trainingWithMaxForUebung[0].gewicht
    aktuelleLeistung.wiederholungen = trainingWithMaxForUebung[0].wiederholungen

    return aktuelleLeistung


def getUebungen():
    uebungen = Uebungen.objects.all()
    return uebungen