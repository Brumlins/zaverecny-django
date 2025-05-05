from django.urls import path
from . import views

urlpatterns = [
    path('recepty/', views.recepty, name='recepty'),
    path('members/', views.members_list, name='members_list'),
]