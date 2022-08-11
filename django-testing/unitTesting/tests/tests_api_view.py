from rest_framework.test import APITestCase
import datetime
from django.urls import reverse
from rest_framework import status

# test_api_view.py
class StudentSerializerTestCase(APITestCase):
    def student_creation_test(self):
        payload = {
            "first_name": "Joan",
            "last_name": "Keith",
            "reg_num": "Abrt1",
            "date_of_admission": datetime.date.today()
        }
        response = self.client.post(reverse("create-student"), payload)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code) 