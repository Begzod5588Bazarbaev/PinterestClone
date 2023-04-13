from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from app.views import *



urlpatterns = [
    path('register/success/', TemplateView.as_view(template_name='registration/success.html'), name='register-success'),
    path('register/', Register.as_view(), name='register'),
    path('password/success/', TemplateView.as_view(template_name='accounts/password_success.html'), name='change_password_success'),
    path('password/', change_password, name='change_password'),
    path('name/', change_name, name='change_name'),
    path('admin/', admin.site.urls),
    path('', include('app.urls'), name='menu'),
    path('', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)