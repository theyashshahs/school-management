from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from guardian.models import Guardian
from guardian.serializers import GuardianSerializer

class GuardianViewSet(ModelViewSet):
    serializer_class = GuardianSerializer
    queryset = Guardian.objects.all()
    