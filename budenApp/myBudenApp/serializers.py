from rest_framework import serializers
from .models import Training, User, Uebungen

class UebungenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uebungen
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        #fields = ["id", "name"]

class TrainingsSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=False)
    uebung = serializers.SerializerMethodField(read_only=False)

    def get_user(self, training):
        return UserSerializer(training.user, many=False, read_only=False).data

    def get_uebung(self, training):
        return UebungenSerializer(training.uebung, many=False, read_only=False).data

    class Meta:
        model = Training
        fields = ["id", "date", "user", "uebung", "gewicht", "wiederholungen", "comment"]


class TrainingsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = "__all__"


class UsersCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

