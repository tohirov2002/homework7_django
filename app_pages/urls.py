
from django.urls import path

from .views import home,about,contact,login,register


urlpatterns = [
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('',home,name='home')
]