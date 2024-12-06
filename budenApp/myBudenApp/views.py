from datetime import datetime
from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Training, Uebungen, User
from rest_framework import generics, permissions
from .repository import getLatestTrainingForUebungAndUser, getLatestGewichtForUebungAndUser, getUebungen, getLatestGewichtAndWiederholungenForUebungAndUser
from .serializers import UebungenSerializer, TrainingsSerializer, UserSerializer, UsersCreateSerializer, TrainingsCreateSerializer, AktuelleLeistungSerializer
from rest_framework.views import APIView

def home(request):
    return render(request, "home.html")

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"

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


class LatestGewichtAndWiederholungenForUebungAndUser(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        userId = kwargs.get('userId')
        uebungId = kwargs.get('uebungId')

        queryset = getLatestGewichtAndWiederholungenForUebungAndUser(userId, uebungId)

        if(queryset == None):
            print("Keine Daten gefunden")
            return Response(data={"status": 404, "data": None})

        serializer_class = AktuelleLeistungSerializer(queryset, many=False)
        return Response(data={"status": 200, "data": serializer_class.data})



#class Uebungen(APIView):
#    def get(self, request):
#        result = getUebungen()
#        print(len(result))
#        serializer_class = UebungenSerializer(result, many=True)
#        return Response(data = {"status": 200, "data": serializer_class.data})

class TrainingsFuerUserList(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        userId = kwargs.get('userId')
        queryset = Training.objects.filter(user__id = userId).order_by('-date')
        serializer_class = TrainingsSerializer(queryset, many=True)
        return Response(data={"status": 200, "data": serializer_class.data})

class TrainingsFuerUserFuerHeutigenTagList(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        userId = kwargs.get('userId')
        queryset = Training.objects.filter(user__id = userId) .filter(date = datetime.now()).order_by('id')
        serializer_class = TrainingsSerializer(queryset, many=True)
        return Response(data={"status": 200, "data": serializer_class.data})




#class TrainingsFuerUserCreateList(generics.CreateAPIView):
#    permission_classes = [permissions.AllowAny, ]
#    queryset = Training.objects.all()
#    serializer_class = TrainingsSerializer

#class UserViewset(ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UsersCreateSerializer

class TrainingViewset(ModelViewSet):
    lookup_field = "pk"
    queryset = Training.objects.all()
    serializer_class = TrainingsCreateSerializer
