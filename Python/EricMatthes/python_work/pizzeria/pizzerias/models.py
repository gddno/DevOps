from django.db import models

# Create your models here.



class Pizza(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
	    return self.name


class Toppings(models.Model):
    name = models.CharField(max_length = 100)
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)

    def __str__(self):
	    return self.name