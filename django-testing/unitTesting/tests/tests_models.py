# test_models.py
from django.test import TestCase
from unitTesting.models import Students

class StudentModelTestcase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Students.objects.create(first_name="Peter", last_name="John", reg_num="111b2")

    def test_string_method(self):
        student = Students.objects.get(id=1)
        expected_string = f"{student.first_name} {student.last_name} has {student.reg_num} registration number"
        self.assertEqual(str(student), expected_string)

    def test_get_absolute_url(self):
        student = Students.objects.get(id=1)
        self.assertEqual(student.get_absolute_url(), "/students/1")