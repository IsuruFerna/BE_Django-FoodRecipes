from django.test import TestCase

from .models import Meal, Category

# Create your tests here.
class CategoryTestCase(TestCase):

    def setUp(self):
        # creates categories
        c1 = Category.objects.create(
            strCategory="Pizza",
            strCategoryTumb="https://www.simplyrecipes.com/thmb/KE6iMblr3R2Db6oE8HdyVsFSj2A=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/__opt__aboutcom__coeus__resources__content_migration__simply_recipes__uploads__2019__09__easy-pepperoni-pizza-lead-3-1024x682-583b275444104ef189d693a64df625da.jpg",
            strCategoryDescription="Pizza is a traditional Italian dish typically consisting of a flat base of leavened wheat-based dough topped with tomato, cheese, and other ingredients, baked at a high temperature, traditionally in a wood-fired oven"
                                     )
        
        c2 = Category.objects.create(
            strCategory="Beef",
            strCategoryTumb="https://www.themealdb.com/images/category/beef.png",
            strCategoryDescription="Beef is the culinary name for meat from cattle, particularly skeletal muscle. Humans have been eating beef since prehistoric times.[1] Beef is a source of high-quality protein and essential nutrients.[2]"
        )

        # create meals
        m1 = Meal.objects.create(
            strMeal = "Beef Wellington",
            strCategory = c2,
            strArea = "British",
            strInstructions =  "Put the mushrooms into a food processor with some seasoning and pulse to a rough paste. Scrape the paste into a pan and cook over a high heat for about 10 mins, tossing frequently, to cook out the moisture from the mushrooms. Spread out on a plate to cool.\r\nHeat in a frying pan and add a little olive oil. Season the beef and sear in the hot pan for 30 secs only on each side. (You don't want to cook it at this stage, just colour it). Remove the beef from the pan and leave to cool, then brush all over with the mustard.\r\nLay a sheet of cling film on a work surface and arrange the Parma ham slices on it, in slightly overlapping rows. With a palette knife, spread the mushroom paste over the ham, then place the seared beef fillet in the middle. Keeping a tight hold of the cling film from the edge, neatly roll the Parma ham and mushrooms around the beef to form a tight barrel shape. Twist the ends of the cling film to secure. Chill for 15-20 mins to allow the beef to set and keep its shape.\r\nRoll out the puff pastry on a floured surface to a large rectangle, the thickness of a £1 coin. Remove the cling film from the beef, then lay in the centre. Brush the surrounding pastry with egg yolk. Fold the ends over, the wrap the pastry around the beef, cutting off any excess. Turn over, so the seam is underneath, and place on a baking sheet. Brush over all the pastry with egg and chill for about 15 mins to let the pastry rest.\r\nHeat the oven to 200C, 400F, gas 6.\r\nLightly score the pastry at 1cm intervals and glaze again with beaten egg yolk. Bake for 20 minutes, then lower the oven setting to 180C, 350F, gas 4 and cook for another 15 mins. Allow to rest for 10-15 mins before slicing and serving with the side dishes of your choice. The beef should still be pink in the centre when you serve it.",
            strMealThumb =  "https://www.themealdb.com/images/media/meals/vvpprx1487325699.jpg",
            strTags = "Meat,Stew",
            strYoutube = 	"https://www.youtube.com/watch?v=FS8u1RBdf6I",
            strIngredient1 ="mushrooms",
            strIngredient2 = "English Mustard", 
            strIngredient3 = "Olive Oil", 
            strSource = "http://www.goodtoknow.co.uk/recipes/164868/Gordon-Ramsay-s-beef-Wellington",
        )

        m2 = Meal.objects.create(
            strMeal = "Beef Wellington not valid ingredients",
            strDrinkAlternate = "",
            strCategory = c2,
            strArea = "British",
            strInstructions =  "Put the mushrooms into a food processor with some seasoning and pulse to a rough paste. Scrape the paste into a pan and cook over a high heat for about 10 mins, tossing frequently, to cook out the moisture from the mushrooms. Spread out on a plate to cool.\r\nHeat in a frying pan and add a little olive oil. Season the beef and sear in the hot pan for 30 secs only on each side. (You don't want to cook it at this stage, just colour it). Remove the beef from the pan and leave to cool, then brush all over with the mustard.",
            strMealThumb =  "https://www.themealdb.com/images/media/meals/vvpprx1487325699.jpg",
            strTags = "Meat,Stew",
            strYoutube = 	"https://www.youtube.com/watch?v=FS8u1RBdf6I",
            strIngredient1 ="mushrooms",
            strIngredient2 = "English Mustard", 
            strIngredient3 = "", 
            strIngredient4 = "", 
            strMeasure1 =  "400g",
            strMeasure2 =  "1-2tbsp",
            strSource = "http://www.goodtoknow.co.uk/recipes/164868/Gordon-Ramsay-s-beef-Wellington",
        )

    # test category
    def test_category_count(self):
        c = Category.objects.all()
        print("this is meal count: ", c.count())
        self.assertEqual(c.count(), 2)

    def test_pizza_exsists(self):
        p = Category.objects.get(strCategory="Pizza")
        self.assertEqual(p.strCategory, "Pizza")
    
    # test meals
    def test_meal_category_and_area(self):
        c = Category.objects.get(strCategory="Beef")
        m = Meal.objects.get(strMeal="Beef Wellington", strCategory=c)
        self.assertEqual(m.strArea, "British")

    def test_meal_count(self):
        m = Meal.objects.all()
        print("this is meal count: ", m.count())
        self.assertEqual(m.count(), 2)

    def test_validate_meal(self):
        c2 = Category.objects.get(strCategory="Beef")
        m = Meal.objects.get(strCategory=c2, strMeal="Beef Wellington")
        self.assertTrue(m.is_valid_meal())

    def test_invalid_meal_ingredients(self):
        c2 = Category.objects.get(strCategory="Beef")
        m = Meal.objects.get(strCategory=c2, strMeal="Beef Wellington not valid ingredients")
        self.assertFalse(m.is_valid_meal())

        
    
