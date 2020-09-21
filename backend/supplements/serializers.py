from rest_framework import serializers
from .models import Functional, Nutrient, Supplement


class FunctionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Functional
        fields = '__all__'


class NutrientSerializer(serializers.ModelSerializer):
    functionals = FunctionalSerializer(many=True)

    class Meta:
        model = Nutrient
        fields = '__all__'


class NutrientSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutrient
        fields = ['id', 'name']


class SupplementListSerializer(serializers.ModelSerializer):
    nutrients = NutrientSimpleSerializer(many=True)

    class Meta:
        model = Supplement
        fields = ['id', 'name', 'nutrients']


class SupplementSerializer(serializers.ModelSerializer):
    nutrients = NutrientSerializer(many=True)

    class Meta:
        model = Supplement
        fields = '__all__'
