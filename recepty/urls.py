from django.urls import path
from . import views

urlpatterns = [
    path('recepty/', views.recepty, name='recepty'),
    path('members/', views.members, name='members'),
    path('members/add/', views.add_member, name='add_member'),
    path('members/delete/<int:member_id>/', views.delete_member, name='delete_member'),
    path('members/edit/<int:member_id>/', views.edit_member, name='edit_member'),
]