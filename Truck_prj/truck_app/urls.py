from django.urls import path
from truck_app import views

urlpatterns = [
    path('', views.index, name='index'),
]
