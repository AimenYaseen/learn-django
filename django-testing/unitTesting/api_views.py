from rest_framework import generics
from .models import Students
from .serializers import StudentSerializer

class CreateStudentAPIView(generics.CreateAPIView):
    query_set = Students.objects.all()
    serializer_class = StudentSerializer