from django.shortcuts import render
from rest_framework.views import APIView
from .models import EmailSub, Location
from .serializers import LocationSerializer, EmailSubSerializer

# Create your views here.

class MailService(APIView):
    def get(self, request, *args, **kwargs):
        pass
                 



