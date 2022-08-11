from .models import Students
from rest_framework.serializers import ModelSerializer

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"