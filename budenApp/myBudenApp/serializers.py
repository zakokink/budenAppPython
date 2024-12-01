from rest_framework import serializers
from .models import Training, User, Uebungen

class UebungenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uebungen
        fields = ["id", "uebung"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name"]

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
    user = serializers.SerializerMethodField(read_only=False)
    uebung = serializers.SerializerMethodField(read_only=False)

    def get_user(self, training):
        return UserSerializer(training.user, many=False, read_only=False).data

    def get_uebung(self, training):
        return UebungenSerializer(training.uebung, many=False, read_only=False).data

    class Meta:
        model = Training
        fields = ["id", "date", "user", "uebung", "gewicht", "wiederholungen", "comment"]
