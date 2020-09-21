from django.db import models

# Create your models here.


class Functional(models.Model):
    category = models.CharField(max_length=50)
    content = models.CharField(max_length=150)


class Nutrient(models.Model):
    name = models.CharField(max_length=50)
    limit_low = models.FloatField()
    limit_high = models.FloatField()
    precaution = models.TextField()
    functionals = models.ManyToManyField(
        Functional,
        related_name="nutrients"
    )


class Supplement(models.Model):
    dosage = models.CharField(max_length=150)
    name = models.CharField(max_length=50)
    expiration_date = models.CharField(max_length=50)
    storage_method = models.TextField(null=True, blank=True)
    manufacturer = models.CharField(max_length=50)
    product_form = models.CharField(max_length=50)
    nutrients = models.ManyToManyField(
        Nutrient,
        related_name='supplements'
    )
