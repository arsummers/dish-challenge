from django.db import models


# The dish description is intended as a short description of the dish, or the name of the dish.
# The other dish text field is intended for optional longer descriptions of the dishes.
# The price is able to take up to $9999.00

class Dish(models.Model):
    img = models.ImageField(upload_to='images/')
    restaurant_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    dish_description = models.CharField(max_length=100)
    other_dish_text = models.CharField(max_length=255)

    def __str__(self):
        return self.dish_description