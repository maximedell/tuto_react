from django.contrib import admin
from django.http import HttpRequest, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import path, reverse
import csv

from .models import (
    Ingredient,
    Recipe,
    Category,
    Step,
    NutritionalValue,
    NutritionalValueGeneric,
)
from .forms import CSVImportForm


class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title", "is_ingredient", "is_final")
    search_fields = ("title",)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "import-csv/",
                self.admin_site.admin_view(self.import_csv),
                name="import_csv_recipe",
            )
        ]
        return custom_urls + urls

    def create_recipe(self, row):
        h_recipe = "recipe"
        h_ingredient = "ingredient"
        h_quantity = "quantity"
        h_is_ingredient = "is_ingredient"
        if not Recipe.objects.filter(title=row[h_recipe]).exists():
            if row[h_is_ingredient] == "1":
                if Ingredient.objects.filter(name=row[h_recipe]).exists():
                    ing = Ingredient.objects.get(name=row[h_recipe])
                else:
                    ing = Ingredient.objects.create(name=row[h_recipe])
                recipe = Recipe.objects.create(
                    title=row[h_recipe],
                    is_ingredient=True,
                    ingredient=ing,
                )
            else:
                recipe = Recipe.objects.create(
                    title=row[h_recipe],
                    is_ingredient=False,
                )

        else:
            recipe = Recipe.objects.get(title=row[h_recipe])
            if row[h_is_ingredient] == "1":
                recipe.is_ingredient = True
                if recipe.ingredient is None:
                    if Ingredient.objects.filter(name=row[h_recipe]).exists():
                        ing = Ingredient.objects.get(name=row[h_recipe])
                    else:
                        ing = Ingredient.objects.create(name=row[h_recipe])
                    recipe.ingredient = ing
                recipe.save()
            else:
                recipe.is_ingredient = False
                recipe.ingredient = None
                recipe.save()
        if not Ingredient.objects.filter(name=row[h_ingredient]).exists():
            ing = Ingredient.objects.create(name=row[h_ingredient])
        else:
            ing = Ingredient.objects.get(name=row[h_ingredient])
        if not Step.objects.filter(recipe=recipe, ingredient=ing).exists():
            Step.objects.create(
                step_text=row[h_ingredient],
                recipe=recipe,
                ingredient=ing,
                quantity=row[h_quantity],
                unit="kg",
                step_number=recipe.steps.count() + 1,
            )

    def import_csv(self, request: HttpRequest):
        if request.method == "POST":
            form = CSVImportForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = request.FILES["csv_file"]
                decoded_file = csv_file.read().decode("utf-8").splitlines()
                reader = csv.DictReader(decoded_file)
                for row in reader:
                    self.create_recipe(row)
                self.message_user(request, "CSV file has been imported successfully")
                return HttpResponseRedirect(reverse("admin:recipe_recipe_changelist"))
        else:
            form = CSVImportForm()

        context = dict(
            self.admin_site.each_context(request),
            opts=self.model._meta,
            app_label=self.model._meta.app_label,
            title="Import CSV",
            form=form,
        )
        return TemplateResponse(request, "admin/import_csv_form.html", context)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "import-csv/",
                self.admin_site.admin_view(self.import_csv),
                name="import_csv_ingredient",
            )
        ]
        return custom_urls + urls

    def import_csv(self, request: HttpRequest):
        if request.method == "POST":
            form = CSVImportForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = request.FILES["csv_file"]
                decoded_file = csv_file.read().decode("utf-8").splitlines()
                reader = csv.DictReader(decoded_file)
                for row in reader:
                    if not Ingredient.objects.filter(name=row["ingredient"]).exists():
                        Ingredient.objects.create(name=row["ingredient"])
                self.message_user(request, "CSV file has been imported successfully")
                return HttpResponseRedirect(
                    reverse("admin:recipe_ingredient_changelist")
                )
        else:
            form = CSVImportForm()

        context = dict(
            self.admin_site.each_context(request),
            opts=self.model._meta,
            app_label=self.model._meta.app_label,
            title="Import CSV",
            form=form,
        )
        return TemplateResponse(request, "admin/import_csv_form.html", context)


class NutritionalValueGenericAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "energy",
        "fat",
        "saturated_fat",
        "carbohydrates",
        "sugar",
        "protein",
        "salt",
        "alcohol",
        "fruits_vegetables_nuts",
    )
    search_fields = ("name",)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "import-csv/",
                self.admin_site.admin_view(self.import_csv),
                name="import_csv_nutritionalvaluegeneric",
            )
        ]
        return custom_urls + urls

    def import_csv(self, request: HttpRequest):
        if request.method == "POST":
            form = CSVImportForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = request.FILES["csv_file"]
                decoded_file = csv_file.read().decode("utf-8").splitlines()
                reader = csv.DictReader(decoded_file)
                for row in reader:
                    NutritionalValueGeneric.objects.create(
                        name=row["Name_FR"],
                        energy=row["Nrj_kcal"],
                        fat=row["Lipides_g"],
                        saturated_fat=row["Ags_g"],
                        carbohydrates=row["Glucides_g"],
                        sugar=row["Sucres_g"],
                        protein=row["Proteines_g"],
                        salt=row["Sel_g"],
                        fruits_vegetables_nuts=row["Fibres_g"],
                    )
                self.message_user(request, "CSV file has been imported successfully")
                return HttpResponseRedirect(
                    reverse("admin:recipe_nutritionalvaluegeneric_changelist")
                )
        else:
            form = CSVImportForm()

        context = dict(
            self.admin_site.each_context(request),
            opts=self.model._meta,
            app_label=self.model._meta.app_label,
            title="Import CSV",
            form=form,
        )
        return TemplateResponse(request, "admin/import_csv_form.html", context)


admin.site.register(NutritionalValueGeneric, NutritionalValueGenericAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
