from django.contrib.auth.models import User
from django.db import models

class AccountModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='account')
    account_type = models.CharField(max_length=20, choices=[('patient', 'Patient'), ('doctor', 'Doctor')])
    nid = models.CharField(max_length=20,unique=True, blank=True, null=True)
    is_activated = models.BooleanField(default=False,null=True , blank = True)
    email_token= models.CharField(max_length=200,null=True , blank = True)

    def __str__(self):
        return self.account_type



