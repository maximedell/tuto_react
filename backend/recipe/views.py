from rest_framework import generics
from .models import (
    Recipe,
    Ingredient,
    Step,
    NutritionalValue,
    NutritionalValueGeneric,
    Category,
)
from .serializers import (
    RecipeSerializer,
    IngredientSerializer,
    StepSerializer,
    NutritionalValueSerializer,
    NutritionalValueGenericSerializer,
    CategorySerializer,
)


class RecipeListCreate(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class IngredientListCreate(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class StepListCreate(generics.ListCreateAPIView):
    queryset = Step.objects.all()
    serializer_class = StepSerializer


class StepRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Step.objects.all()
    serializer_class = StepSerializer


class NutritionalValueListCreate(generics.ListCreateAPIView):
    queryset = NutritionalValue.objects.all()
    serializer_class = NutritionalValueSerializer


class NutritionalValueRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = NutritionalValue.objects.all()
    serializer_class = NutritionalValueSerializer


class NutritionalValueGenericListCreate(generics.ListCreateAPIView):
    queryset = NutritionalValueGeneric.objects.all()
    serializer_class = NutritionalValueGenericSerializer


class NutritionalValueGenericRetrieveUpdateDestroy(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = NutritionalValueGeneric.objects.all()
    serializer_class = NutritionalValueGenericSerializer


class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
