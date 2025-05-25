from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Ingredient, Recipe
from .forms import RecipeForm, RecipeIngredientFormSet, IngredientForm, RegistraceForm


def profile(request):
    return render(request, 'profile.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def registrace(request):
    if request.method == "POST":
        form = RegistraceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Po úspěšné registraci přesměruj na přihlášení
    else:
        form = RegistraceForm()
    return render(request, 'registration/registrace.html', {'form': form})



def index(request):
    return render(request, 'index.html')  # Ukázková domovská stránka


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recepty/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.ingredients.all()
    return render(request, 'recepty/recipe_detail.html', {'recipe': recipe})


@login_required
def pridat_ingredienci(request):
    if request.method == "POST":
        form = IngredientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm()
    return render(request, 'ingredience/pridat_ingredienci.html', {'form': form})

def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'ingredience/ingredient_list.html', {'ingredients': ingredients})

def ingredient_detail(request, name):
    ingredient = Ingredient.objects.get(name=name)
    recepty = ingredient.recipeingredient_set.all()  # všechny RecipeIngredient záznamy s touto ingrediencí
    return render(request, 'ingredience/ingredient_detail.html', {
        'ingredient': ingredient,
        'recepty': recepty,
    })



@login_required
def pridat_recept(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        formset = RecipeIngredientFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            recipe = form.save(commit=False)
            recipe.autor = request.user
            recipe.save()
            formset.instance = recipe
            formset.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
        formset = RecipeIngredientFormSet()
    return render(request, 'recepty/pridat_recept.html', {'form': form, 'formset': formset})


