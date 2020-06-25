from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from administration.models import Class, Fee
from administration.serializers import ClassSerializer, FeeSerializer

class ClassViewSet(ModelViewSet):
    serializer_class = ClassSerializer
    queryset = Class.objects.all()


class FeeViewSet(ModelViewSet):
    serializer_class = FeeSerializer
    queryset = Fee.objects.all()