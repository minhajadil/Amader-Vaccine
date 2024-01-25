from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('Account.urls')),
    path('', views.homepage,name='homepage'),
    path('doctor/',include('Doctor.urls')),
    path('patient/',include('Patient.urls')),
    path('blog/',include('Blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
