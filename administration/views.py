from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from administration.models import Course
from administration.serializers import CourseSerializer

class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
