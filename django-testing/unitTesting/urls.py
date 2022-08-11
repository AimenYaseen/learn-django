from django.urls import path
from .views import StudentListView, StudentDetailView
from .api_views import CreateStudentAPIView

urlpatterns = [
    path('', StudentListView.as_view(), name="students"),
    path('create', CreateStudentAPIView.as_view(), name="create-student"),
    path('<int:pk>', StudentDetailView.as_view(), name="student-detail")
]