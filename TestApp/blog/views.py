from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Userserializer
from django.contrib.auth.models import User

class UserView(viewsets.ModelViewSet):
    serializer_class=Userserializer
    queryset=User.objects.all().order_by('-date_joined')