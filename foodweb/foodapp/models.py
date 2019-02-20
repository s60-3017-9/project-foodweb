from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    number = models.CharField(max_length=20)
    time = models.CharField(max_length=200)
    location = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Reviews(models.Model):
    reviews = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    reviews_text = models.CharField(max_length=500)
    point = models.IntegerField(default=0)


