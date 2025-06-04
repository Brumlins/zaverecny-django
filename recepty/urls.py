from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .forms import VlastniLoginForm
urlpatterns = [
    path('', views.index, name='index'),

    path('login/', auth_views.LoginView.as_view(authentication_form=VlastniLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='logout'), name='logout'),
    path('accounts/profile/', login_required(views.profile), name='profile'),
    path('registrace/', views.registrace, name='registrace'),

    path('recepty/pridat/', views.pridat_recept, name='pridat_recept'),
    path('recepty/', views.recipe_list, name='recipe_list'),
    path('recepty/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recepty/<int:pk>/edit/', views.recipe_edit, name='recipe_edit'),

    path('ingredience/pridat/', views.pridat_ingredienci, name='pridat_ingredienci'),
    path('ingredience/', views.ingredient_list, name='ingredient_list'),
    path('ingredience/<str:name>/', views.ingredient_detail, name='ingredient_detail'),


]
