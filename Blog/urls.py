from django.urls import path
from .import views

urlpatterns = [
    path('add/',views.add_post,name='add_post'),
    path('details/<int:id>',views.post_details,name='post_details'),
    path('all/',views.all_blogs,name='all_blogs'),
]