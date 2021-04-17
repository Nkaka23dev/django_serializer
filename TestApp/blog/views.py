from rest_framework import viewsets
from .serializers import Userserializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class UserView(viewsets.ModelViewSet):
    serializer_class=Userserializer
    queryset=User.objects.all().order_by('-date_joined')
    authentication_classes=(TokenAuthentication,)
    # permission_classes=(IsAuthenticated,)