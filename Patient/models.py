from django.db import models
from Doctor.models import Vaccine
from django.contrib.auth.models import User
# Create your models here.

class VaccineTaken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='vaccine_taken_by',null=True)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE,related_name='vaccine')
    date_taken = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f"{self.user.username} took {self.vaccine}"
    





