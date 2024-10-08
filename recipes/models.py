from django.db import models

import uuid

from users.models import CustomUser

class Category(models.Model):
    idCategory = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="categories")
    strCategory = models.CharField(max_length=64)
    strCategoryTumb = models.URLField(max_length=300)
    strCategoryDescription = models.TextField()

    def __str__(self):
        return f"Category: {self.strCategory}, id: {self.idCategory}"


class Meal(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="meals")
    strCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    idMeal = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    strMeal = models.CharField(max_length=200)
    strDrinkAlternate = models.CharField(null=True, blank=True, max_length=64)
    strArea = models.CharField(max_length=64, blank=True)
    strInstructions =  models.TextField(max_length=5000)
    strMealThumb =  models.URLField(blank=True)
    strTags = models.CharField(blank=True, max_length=200)
    strYoutube = models.URLField(blank=True)
    strIngredient1 = models.CharField(max_length=64, blank=True) 
    strIngredient2 = models.CharField(max_length=64, blank=True) 
    strIngredient3 = models.CharField(max_length=64, blank=True) 
    strIngredient4 = models.CharField(max_length=64, blank=True) 
    strIngredient5 = models.CharField(max_length=64, blank=True) 
    strIngredient6 = models.CharField(max_length=64, blank=True) 
    strIngredient7 = models.CharField(max_length=64, blank=True) 
    strIngredient8 = models.CharField(max_length=64, blank=True) 
    strIngredient9 = models.CharField(max_length=64, blank=True) 
    strIngredient10 = models.CharField(max_length=64, blank=True) 
    strIngredient11 = models.CharField(max_length=64, blank=True) 
    strIngredient12 = models.CharField(max_length=64, blank=True) 
    strIngredient13 = models.CharField(max_length=64, blank=True) 
    strIngredient14 = models.CharField(max_length=64, blank=True) 
    strIngredient15 = models.CharField(max_length=64, blank=True) 
    strIngredient16 = models.CharField(max_length=64, blank=True) 
    strIngredient17 = models.CharField(max_length=64, blank=True) 
    strIngredient18 = models.CharField(max_length=64, blank=True) 
    strIngredient19 = models.CharField(max_length=64, blank=True) 
    strIngredient20 = models.CharField(max_length=64, blank=True) 
    strMeasure1 =  models.CharField(max_length=60, blank=True)
    strMeasure2 =  models.CharField(max_length=60, blank=True)
    strMeasure3 =  models.CharField(max_length=60, blank=True)
    strMeasure4 =  models.CharField(max_length=60, blank=True)
    strMeasure5 =  models.CharField(max_length=60, blank=True)
    strMeasure6 =  models.CharField(max_length=60, blank=True)
    strMeasure7 =  models.CharField(max_length=60, blank=True)
    strMeasure8 =  models.CharField(max_length=60, blank=True)
    strMeasure9 =  models.CharField(max_length=60, blank=True)
    strMeasure10 =  models.CharField(max_length=60, blank=True)
    strMeasure11 =  models.CharField(max_length=60, blank=True)
    strMeasure12 =  models.CharField(max_length=60, blank=True)
    strMeasure13 =  models.CharField(max_length=60, blank=True)
    strMeasure14 =  models.CharField(max_length=60, blank=True)
    strMeasure15 =  models.CharField(max_length=60, blank=True)
    strMeasure16 =  models.CharField(max_length=60, blank=True)
    strMeasure17 =  models.CharField(max_length=60, blank=True)
    strMeasure18 =  models.CharField(max_length=60, blank=True)
    strMeasure19 =  models.CharField(max_length=60, blank=True)
    strMeasure20 =  models.CharField(max_length=60, blank=True)
    strSource = models.URLField(blank=True)
    strImageSource = models.URLField(blank=True)
    strCreativeCommonsConfirmed = models.BooleanField(blank=True, null=True)
    dateModified = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Meal: {self.strMeal}, id: {self.idMeal}, category: {self.strCategory}"
    
    def is_valid_meal(self):
        at_lest_three_must_not_empty = False
        ingredients = [
            self.strIngredient1,
            self.strIngredient2,
            self.strIngredient3,
            self.strIngredient4,
            self.strIngredient5,
            self.strIngredient6,
            self.strIngredient7,
            self.strIngredient8,
            self.strIngredient9,
            self.strIngredient10,
            self.strIngredient11,
            self.strIngredient12,
            self.strIngredient13,
            self.strIngredient14,
            self.strIngredient15,
            self.strIngredient16,
            self.strIngredient17,
            self.strIngredient18,
            self.strIngredient19,
            self.strIngredient20,
        ]
        
        # checks if there are at least 3 ingredients
        if len([i for i in ingredients if i]) >= 3:
            at_lest_three_must_not_empty = True

        return len(self.strInstructions) < 5000 and self.strCategory and len(self.strMeal) < 200 and at_lest_three_must_not_empty


