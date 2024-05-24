from rest_framework import serializers
from .models import (
    Recipe,
    Ingredient,
    Step,
    NutritionalValue,
    NutritionalValueGeneric,
    Category,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class NutritionalValueGenericSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionalValueGeneric
        fields = "__all__"


class NutritionalValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionalValue
        fields = "__all__"


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = "__all__"


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class RecipeSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True)
    nutritional_value = NutritionalValueSerializer()
    category = CategorySerializer()

    class Meta:
        model = Recipe
        fields = "__all__"
