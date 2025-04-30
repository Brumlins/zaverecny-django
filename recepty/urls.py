from django.urls import path
from . import views

urlpatterns = [
    path('recepty/', views.recepty, name='recepty'),
]