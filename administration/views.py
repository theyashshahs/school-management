from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from administration.models import Class
from administration.serializers import ClassSerializer

class ClassViewSet(ModelViewSet):
    serializer_class = ClassSerializer
    queryset = Class.objects.all()
