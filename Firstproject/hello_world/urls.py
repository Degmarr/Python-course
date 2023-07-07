
from django.urls import path
from .views import *

urlpatterns = [
    path('', Mainpage, name = 'MainPage'),
]
