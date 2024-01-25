from django.db import models
from django.contrib.auth.models import User
from Account.models import AccountModel
from datetime import timedelta

class Vaccine(models.Model):
    images = models.ImageField(upload_to='vaccines/uploads/',null=True ,blank=True)
    doctor = models.ForeignKey(AccountModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True ,blank=True)
    initial_dose = models.DateTimeField(max_length=50)  
    second_dose = models.DateTimeField(null=True, blank=True)
    third_dose = models.DateTimeField(null=True, blank=True)

    def generate_second_dose(self):
        if self.initial_dose:
            self.second_dose = self.initial_dose + timedelta(days=30)
            self.save()

    def generate_third_dose(self):
       
        if self.second_dose:
            self.third_dose = self.second_dose + timedelta(days=30)
            self.save()

    def save(self, *args, **kwargs):
        if not self.second_dose:
            self.generate_second_dose()
        if not self.third_dose:
            self.generate_third_dose()
        super().save(*args, **kwargs)



class Comment(models.Model):
    Vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments',null=True)
    Comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    