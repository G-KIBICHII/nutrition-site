from django.db import models

# Create your models here.
class logg(models.Model):
    user=models.CharField(max_length=100)
    passer=models.CharField(max_length=100)
class cereal(models.Model):
    name=models.CharField(max_length=40,unique=True) 	
    calories=models.IntegerField()	
    protein=models.IntegerField()	
    fat=models.IntegerField()	
    sodium=models.IntegerField()	
    fiber=models.FloatField()	
    carbo=models.FloatField()	
    sugars=models.IntegerField()	
    potass=models.IntegerField()	
    vitamins=models.IntegerField()	
    rating=models.FloatField()

    