from django.db import models

# Create your models here.
class Category(models.Model):
    idCategory = models.AutoField(primary_key=True)
    strCategory = models.CharField(max_length=64)
    strCategoryTumb = models.URLField()
    strCategoryDescription = models.TextField()

    def __str__(self):
        return f"Category: {self.strCategory}, id: {self.idCategory}"


class Meal(models.Model):
    idMeal = models.AutoField(primary_key=True)
    strMeal = models.CharField(max_length=200)
    strDrinkAlternate = models.CharField(null=True, blank=True, max_length=64)
    strCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
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
    strCreativeCommonsConfirmed = models.BooleanField(blank=True)
    dateModified = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Meal: {self.strMeal}, id: {self.idMeal}, category: {self.strCategory}"


