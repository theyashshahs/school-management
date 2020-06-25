from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from teacher.serializers import TeacherSerializer, AssignmentSerializer
from teacher.models import Teacher, Assignment

class TeacherViewSet(ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all() 

class AssignmentViewSet(ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
