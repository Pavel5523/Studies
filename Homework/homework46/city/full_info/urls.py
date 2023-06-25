from django.urls import path
from . import views

urlpatterns = [
    path('', views.full_info, name='full_info'),
]