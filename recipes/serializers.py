from rest_framework import serializers
from .models import Category, Meal

# https://www.django-rest-framework.org/api-guide/relations/

# removing "read_only=False" and adding "queryset=Category.objects.all()" to let know the serializer to where to check to validate data
class MealSerializer(serializers.ModelSerializer):
    # user = serializers.UUIDField(required=False)
    strCategory = serializers.SlugRelatedField(
        slug_field='strCategory',
        queryset=Category.objects.all()
    )

    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='id'
    )

    class Meta:
        model = Meal
        fields = '__all__'
