from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from administration.models import Course, Fees
from administration.serializers import CourseSerializer, FessSerializer

class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class FeesViewSet(ModelViewSet):
    serializer_class = FessSerializer
    queryset = Fees.objects.all()