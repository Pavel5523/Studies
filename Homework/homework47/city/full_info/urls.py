from django.urls import path
from . import views

urlpatterns = [
    path('', views.full_info, name='full_info'),
    path('<int:info_id>/', views.detail, name='detail'),
]