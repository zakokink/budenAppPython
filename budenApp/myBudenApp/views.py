from django.db.models.expressions import result
from django.shortcuts import render,HttpResponse
from rest_framework.response import Response

from .models import Training, Uebungen, User
from django.db.models import Max
from django.core import serializers
from rest_framework import generics, permissions
from .repository import getLatestTrainingForUebungAndUser, getLatestGewichtForUebungAndUser, getUebungen
from .serializers import UebungenSerializer, TrainingsSerializer, UserSerializer
from rest_framework.views import APIView

def home(request):
    return render(request, "home.html")

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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
            return Response(data={"data": None})

        serializer_class = TrainingsSerializer(queryset, many=True)
        return Response(data={"data": serializer_class.data})

class LatestGewichtForUebungAndUser(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        userId = kwargs.get('userId')
        uebungId = kwargs.get('uebungId')

        queryset = getLatestGewichtForUebungAndUser(userId, uebungId)

        if(queryset == None):
            print("Keine Daten gefunden")
            return Response(data={"status": 404, "data": None})

        return Response(data={"status": 200, "data": queryset})

class Uebungen(APIView):
    def get(self, request):
        result = getUebungen()
        print(len(result))
        serializer_class = UebungenSerializer(result, many=True)
        return Response(data = {"status": 200, "data": serializer_class.data})



class TrainingsFuerUserList(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        userId = kwargs.get('userId')
        queryset = Training.objects.filter(user__id = userId).order_by('-date')
        serializer_class = TrainingsSerializer(queryset, many=True)
        return Response(data={"status": 200, "data": serializer_class.data})



class TrainingsFuerUserCreateList(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny, ]
    queryset = Training.objects.all()
    serializer_class = TrainingsSerializer




