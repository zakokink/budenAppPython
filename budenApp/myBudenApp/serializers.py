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
    user = serializers.SerializerMethodField()
    uebung = serializers.SerializerMethodField()

    #user = serializers.StringRelatedField(many=False)
    #uebung = serializers.StringRelatedField(many=False)

    def get_user(self, training):
        return UserSerializer(training.user, many=False).data

    def get_uebung(self, training):
        return UebungenSerializer(training.uebung, many=False).data

    class Meta:
        model = Training
        fields = ["id", "date", "user", "uebung", "gewicht", "wiederholungen", "comment"]

