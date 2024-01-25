from django.urls import path
from .import views

urlpatterns = [
   path('add/',views.create_vaccine,name='add_vaccine'),
   path('edit/<int:id>',views.edit_vaccine,name='edit_vaccine'),
   path('delete/<int:id>',views.delete_vaccine,name='delete_vaccine'),
   path('vaccine_details/<int:id>',views.details,name='vaccine_details'),
   path('comment/<int:id>',views.comment,name='comment'),
   path('all/',views.all_vaccines,name='all_vaccines'),
 
]