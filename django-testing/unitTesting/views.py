from django.views import generic
from unitTesting.models import Students

# List View.
class StudentListView(generic.ListView):
    model = Students
    paginate_by = 10 # the number of students to return in each page

# Detail View.
class StudentDetailView(generic.DetailView):
    model = Students