from django.contrib.auth.models import User
from django.http import response
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from guardian.models import Guardian
from student.models import Student


class GuardianTests(TestCase):
    def setUp(self):
        self.guardian = Guardian.objects.create(student=1, name="optimus")

    def test_get_all_guardian(self):
        response = self.client.get("/guardian/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
