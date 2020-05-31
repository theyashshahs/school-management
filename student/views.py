from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from student.serializers import StudentSerializer
from student.models import Student


class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()