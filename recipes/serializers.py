from rest_framework.serializers import ModelSerializer, SlugRelatedField
from .models import Meal

# https://www.django-rest-framework.org/api-guide/relations/
class MealSerializer(ModelSerializer):
    strCategory = SlugRelatedField(
        read_only=True,
        slug_field='strCategory'
    )

    class Meta:
        model = Meal
        fields = '__all__'
