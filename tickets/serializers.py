from rest_framework import serializers

from tickets.models import *

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Movie

class GeustSerializer(serializers.ModelSerializer):
    class Meta:
        fields =['pk','reservation','name','phone']
        model = Geust

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Reservation