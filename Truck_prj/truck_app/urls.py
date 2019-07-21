from django.urls import path
from truck_app import views

urlpatterns = [
    path('', views.truck_info, name='truck_info'),
]
