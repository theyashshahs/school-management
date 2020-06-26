from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from fees.models import Fee
from fees.serializers import FeeSerializer


class FeeViewSet(ModelViewSet):
    serializer_class = FeeSerializer
    queryset = Fee.objects.all()
