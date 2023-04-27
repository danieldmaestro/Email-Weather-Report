from rest_framework import serializers
from .models import EmailSub, Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"

class EmailSubSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailSub
        fields = "__all__"
        