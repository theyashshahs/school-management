from django.contrib.auth.models import User
from django.http import response
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

from teacher.models import Teacher


class TeacherTests(TestCase):
    def setUp(self):
        self.teacher = Teacher.objects.create(
            teacher_id=1, first_name="optimus", last_name="prime"
        )

    def test_get_all_guardian(self):
        response = self.client.get("/teachers/teacher/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
