from django.db.models.expressions import result
from django.shortcuts import render,HttpResponse
from rest_framework.response import Response

from .models import Training, Uebungen, User
from django.db.models import Max
from django.core import serializers
from rest_framework import generics
from .repository import getLatestTrainingForUebungAndUser, getLatestGewichtForUebungAndUser, getUebungen
from .serializers import UebungenSerializer, TrainingsSerializer
from rest_framework.views import APIView

def home(request):
    return render(request, "home.html")

class UebungenListCreate(generics.ListCreateAPIView):
    queryset = Uebungen.objects.all()
    serializer_class = UebungenSerializer

class UebungenListUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Uebungen.objects.all()
    serializer_class = UebungenSerializer
    lookup_field = "pk"

class LatestTrainingFuerUebungAndUser(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        userId = kwargs.get('userId')
        uebungId = kwargs.get('uebungId')

        queryset = getLatestTrainingForUebungAndUser(userId, uebungId)
        if(queryset == None):
            print("Keine Daten gefunden")
            return Response(data={"letztesTrainingFuerUebung": None})

        serializer_class = TrainingsSerializer(queryset, many=True)
        return Response(data={"letztesTrainingFuerUebung": serializer_class.data})

class LatestGewichtForUebungAndUser(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        userId = kwargs.get('userId')
        uebungId = kwargs.get('uebungId')

        queryset = getLatestGewichtForUebungAndUser(userId, uebungId)
        if(queryset == None):
            print("Keine Daten gefunden")
            return Response(data={"letztesGewichtFuerUebung": None})
        return Response(data={"letztesGewichtFuerUebung": queryset})

class Uebungen(APIView):
    def get(self, request):
        result = getUebungen()
        print(len(result))
        serializer_class = UebungenSerializer(result, many=True)
        return Response(data = {"my_return_data": serializer_class.data})


