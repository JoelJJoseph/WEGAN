from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('Disease/', views.disease, name="disease")
]