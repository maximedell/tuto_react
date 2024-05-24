from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Nom")

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Nom")
    commercial_name = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Nom commercial"
    )
    mk_code = models.CharField(
        max_length=200, verbose_name="Code MK", blank=True, null=True
    )
    status = models.CharField(
        max_length=200, verbose_name="Statut", blank=True, null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        default=None,
        null=True,
        verbose_name="Catégorie",
    )
    PACKAGING_CHOICES = [
        ("gd", "Grand"),
        ("moy", "Moyen"),
        ("pt", "Petit"),
    ]
    packaging_type = models.CharField(
        max_length=4,
        choices=PACKAGING_CHOICES,
        verbose_name="Type d'emballage",
        blank=True,
        null=True,
    )
    net_weight = models.FloatField(verbose_name="Poids net", blank=True, null=True)
    ref_deli = models.CharField(
        max_length=200, verbose_name="Référence DELI", blank=True, null=True
    )
    ref_ean = models.CharField(
        max_length=200, verbose_name="Référence EAN", blank=True, null=True
    )
    ref_efl = models.CharField(
        max_length=200, verbose_name="Référence EFL", blank=True, null=True
    )
    foodcost = models.FloatField(
        verbose_name="Coût de la matière première", blank=True, null=True
    )
    packaging_price = models.FloatField(
        verbose_name="Prix de l'emballage", blank=True, null=True
    )
    workcost = models.FloatField(
        verbose_name="Coût de la main d'oeuvre", blank=True, null=True
    )
    profit_margin = models.FloatField(
        verbose_name="Marge bénéficiaire", blank=True, null=True
    )

    selling_price = models.FloatField(
        verbose_name="Prix de vente", blank=True, null=True
    )
    DLC = models.DateField(
        verbose_name="Date limite de consommation", blank=True, null=True
    )
    technical_sheet = models.FileField(
        upload_to="technical_sheets/",
        verbose_name="Fiche technique",
        blank=True,
        null=True,
    )
    correction_ratio = models.FloatField(
        verbose_name="Ratio de correction", blank=True, null=True
    )

    @property
    def total_cost(self):
        return self.foodcost + self.packaging_price + self.workcost

    @property
    def cost_price(self):
        return self.total_cost * (self.profit_margin + 1)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="Titre")
    is_ingredient = models.BooleanField(default=False, verbose_name="Ingrédient")
    is_final = models.BooleanField(default=False, verbose_name="Produit fini")
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, default=None, null=True
    )

    def __str__(self):
        return self.title

    @property
    def get_total_weight(self):
        total_weight = 0
        for step in self.steps.all():
            total_weight += step.quantity
        return total_weight


class NutritionalValue(models.Model):
    energy = models.FloatField(verbose_name="Énergie (kcal)")
    fat = models.FloatField(verbose_name="Matières grasses")
    saturated_fat = models.FloatField(verbose_name="Acides gras saturés")
    carbohydrates = models.FloatField(verbose_name="Glucides")
    sugar = models.FloatField(verbose_name="Sucres")
    protein = models.FloatField(verbose_name="Protéines")
    salt = models.FloatField(verbose_name="Sel")
    alcohol = models.FloatField(verbose_name="Alcool")
    fruits_vegetables_nuts = models.FloatField(verbose_name="Fruits, légumes, noix")
    ingredient = models.ForeignKey("Ingredient", on_delete=models.CASCADE, default=None)


class Step(models.Model):
    step_text = models.CharField(max_length=200)
    step_number = models.IntegerField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="steps")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()
    UNIT_CHOICES = [
        ("kg", "Kilogramme"),
        ("l", "Litre"),
    ]
    unit = models.CharField(max_length=4, choices=UNIT_CHOICES)

    def __str__(self):
        return self.step_text


class NutritionalValueGeneric(models.Model):
    energy = models.FloatField(verbose_name="Énergie (kcal)")
    fat = models.FloatField(verbose_name="Matières grasses")
    saturated_fat = models.FloatField(verbose_name="Acides gras saturés")
    carbohydrates = models.FloatField(verbose_name="Glucides")
    sugar = models.FloatField(verbose_name="Sucres")
    protein = models.FloatField(verbose_name="Protéines")
    salt = models.FloatField(verbose_name="Sel")
    alcohol = models.FloatField(verbose_name="Alcool", null=True, blank=True)
    fruits_vegetables_nuts = models.FloatField(verbose_name="Fruits, légumes, noix")
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
