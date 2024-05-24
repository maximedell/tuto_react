from django.urls import path
from .views import (
    IngredientListCreate,
    IngredientRetrieveUpdateDestroy,
    CategoryListCreate,
    CategoryRetrieveUpdateDestroy,
    RecipeListCreate,
    RecipeRetrieveUpdateDestroy,
    StepListCreate,
    StepRetrieveUpdateDestroy,
    NutritionalValueListCreate,
    NutritionalValueRetrieveUpdateDestroy,
    NutritionalValueGenericListCreate,
    NutritionalValueGenericRetrieveUpdateDestroy,
)

urlpatterns = [
    path("categories/", CategoryListCreate.as_view(), name="category-list-create"),
    path(
        "categories/<int:pk>/",
        CategoryRetrieveUpdateDestroy.as_view(),
        name="category-retrieve-update-destroy",
    ),
    path("ingredients/", IngredientListCreate.as_view(), name="ingredient-list-create"),
    path(
        "ingredients/<int:pk>/",
        IngredientRetrieveUpdateDestroy.as_view(),
        name="ingredient-retrieve-update-destroy",
    ),
    path("recipes/", RecipeListCreate.as_view(), name="recipe-list-create"),
    path(
        "recipes/<int:pk>/",
        RecipeRetrieveUpdateDestroy.as_view(),
        name="recipe-retrieve-update-destroy",
    ),
    path("steps/", StepListCreate.as_view(), name="step-list-create"),
    path(
        "steps/<int:pk>/",
        StepRetrieveUpdateDestroy.as_view(),
        name="step-retrieve-update-destroy",
    ),
    path(
        "nutritional-values/",
        NutritionalValueListCreate.as_view(),
        name="nutritional-value-list-create",
    ),
    path(
        "nutritional-values/<int:pk>/",
        NutritionalValueRetrieveUpdateDestroy.as_view(),
        name="nutritional-value-retrieve-update-destroy",
    ),
    path(
        "nutritional-values-generic/",
        NutritionalValueGenericListCreate.as_view(),
        name="nutritional-value-generic-list-create",
    ),
    path(
        "nutritional-values-generic/<int:pk>/",
        NutritionalValueGenericRetrieveUpdateDestroy.as_view(),
        name="nutritional-value-generic-retrieve-update-destroy",
    ),
]


# Compare this snippet from backend/recipe/views.py:
