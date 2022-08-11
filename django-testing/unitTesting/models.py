from django.db import models
from django.urls import reverse

# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    reg_num = models.CharField(max_length=25)
    date_of_birth = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])

    def __str__(self):
        return f"{self.first_name} {self.last_name} has {self.reg_num} registration number"