from django.urls import path, include
from django.conf import settings
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.index, name='student'),
]