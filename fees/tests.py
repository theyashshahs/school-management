import datetime

from django.http import response
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

from fees.models import Fee
from student.models import Student


class FeeTests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

        self.fee = Fee.objects.create(student=1,
                                      fees=100000,
                                      dateofpayment=datetime.date.today)

    def test_get_all_fees(self):
        response = self.client.get("/fees/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
