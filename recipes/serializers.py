from rest_framework import serializers
from .models import Meal

# https://www.django-rest-framework.org/api-guide/relations/
class MealSerializer(serializers.ModelSerializer):
    # user = serializers.UUIDField(required=False)
    strCategory = serializers.SlugRelatedField(
        read_only=True,
        slug_field='strCategory'
    )

    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='id'
    )

    class Meta:
        model = Meal
        fields = '__all__'
