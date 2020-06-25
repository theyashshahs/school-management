from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from student.serializers import StudentSerializer, AnswerSerializer
from student.models import Student, Answer


class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class AnswerViewSet(ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()