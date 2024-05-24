from django.forms.models import inlineformset_factory
from django import forms
from .models import Recipe, Ingredient, NutritionalValue

NutritionalValueFormSet = inlineformset_factory(
    Ingredient, NutritionalValue, fields="__all__", extra=1, can_delete=False
)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "is_ingredient", "is_final"]
        # change widget to select
        widgets = {
            "is_ingredient": forms.Select(choices=((True, "Oui"), (False, "Non"))),
            "is_final": forms.Select(choices=((True, "Oui"), (False, "Non"))),
        }


class CSVImportForm(forms.Form):
    csv_file = forms.FileField(
        label="CSV File",
    )
