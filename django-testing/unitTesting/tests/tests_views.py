from django.test import TestCase
from django.urls import reverse
from unitTesting.models import Students
from unitTesting.views import StudentDetailView

class StudentListViewTest(TestCase):
    #setUp Method
    def setUp(self) -> None:
        number_of_students = 30
        for std_id in range(number_of_students):
            Students.objects.create(first_name=f"Aimen{std_id}", last_name="Yaseen")

    def test_url_exists(self):
        import pdb; pdb.set_trace()
        response = self.client.get('/students/')
        code = response.status_code
        self.assertEqual(code, 200)

    def test_url_accessible_by_name(self):
        # import pdb; pdb.set_trace()
        response = self.client.get(reverse('students'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('students'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'unitTesting/students_list.html')

    def test_pagination_is_correct(self):
        response = self.client.get(reverse('students'))
        print(response.context)
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['students_list']), 10)

class StudentDetailViewTest(TestCase):
    
    def test_view_name(self):
        response = self.client.get('/students/', id=1, HTTP_ACCEPT='application/json')
        # self.assertEqual(response.resolver_match.func.__name__, StudentDetailView.as_view().__name__)
        print("Template", response.templates[0].name)
        # print("Client", response.client)
        # print("Context", response.context)
        # print("Content", response.content)
        print("Request", response.request)