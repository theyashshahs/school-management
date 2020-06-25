from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from authentication.models import Auth
from authentication.serializers import AuthSerializer

class AuthViewSet(ModelViewSet):
    serializer_class = AuthSerializer
    queryset = Auth.objects.all()
