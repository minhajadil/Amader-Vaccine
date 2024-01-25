from django.urls import path,include
from .import views

urlpatterns = [
    
    path('takevaccine/<int:id>', views.take_vaccine,name='takevaccine'),
       

  
]
