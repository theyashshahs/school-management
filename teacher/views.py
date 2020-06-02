from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from teacher.serializers import TeacherSerializer
from teacher.models import Teacher

class TeacherViewSet(ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all() 
