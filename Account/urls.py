from django.urls import path
from .import views
urlpatterns = [
   
    path('user/register',views.signup_user.as_view(),name='user_signup'),
    path('doctor/register/',views.signup_doctor.as_view(),name='doctor_signup'),
    path('login/',views.login_user.as_view(),name='login'),
    path('logout/',views.userlogout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('changedata/<int:id>',views.changeuserdata.as_view(),name='changedata'),
    path('changepassword/',views.passchange,name='passchange1'),
    path('changepassword1/',views.passchangewithoutprev,name='passchange2'),
    path('verify/<str:token>',views.verify,name='verify')

]
