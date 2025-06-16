from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profily"


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='ingredient_images/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']  # Řazení podle jména


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recepty')
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']  # Nejnovější recepty nahoře


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100, blank=True, null=True)  # Volitelně prázdné

    def __str__(self):
        return f"{self.quantity} {self.ingredient.name} do {self.recipe.title}"

    class Meta:
        unique_together = ['recipe', 'ingredient']  # Každá ingredience v receptu pouze jednou
