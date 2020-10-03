from django.contrib import admin
from .models import Supplement, Nutrient, Functional, Category
# Register your models here.

admin.site.register([Supplement, Nutrient, Functional, Category])
