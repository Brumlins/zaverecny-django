from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Ingredient, Recipe, RecipeIngredient

from django.forms import inlineformset_factory

from django.contrib.auth.forms import AuthenticationForm

class VlastniLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input'})


class RegistraceForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Tento email je již použitý.")
        return email


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input'})


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'description', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'input'})
        self.fields['description'].widget.attrs.update({'class': 'input'})
        self.fields['image'].widget.attrs.update({'class': 'file-input'})


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'title' in self.fields:
            self.fields['title'].widget.attrs.update({'class': 'input'})
        if 'description' in self.fields:
            self.fields['description'].widget.attrs.update({'class': 'textarea'})
        if 'image' in self.fields:
            self.fields['image'].widget.attrs.update({'class': 'file-input'})


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'quantity' in self.fields:
            self.fields['quantity'].widget.attrs.update({'class': 'input'})


RecipeIngredientFormSet = inlineformset_factory(
    Recipe, RecipeIngredient,
    form=RecipeIngredientForm,
    extra=3,
    can_delete=False
)

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields.values():
        if field.widget.input_type == 'text':
            field.widget.attrs.update({'class': 'input'})
        elif field.widget.input_type == 'textarea':
            field.widget.attrs.update({'class': 'textarea'})
        elif field.widget.input_type == 'file':
            field.widget.attrs.update({'class': 'file-input'})
