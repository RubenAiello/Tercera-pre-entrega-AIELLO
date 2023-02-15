from django.db import models

# Create your models here.

class Autos(models.Model):
    marca=models.CharField(max_length=60)
    modelo=models.CharField(max_length=60)
    fabricacion=models.DateField
    
    def __str__(self) :
        return self.marca
    
class Bicicletas(models.Model):
    marca=models.CharField(max_length=60)
    modelo=models.CharField(max_length=60)
    fabricacion=models.DateField
    
    def __str__(self) :
        return self.marca    
    
class Cuatriciclos(models.Model):
    marca=models.CharField(max_length=60)
    modelo=models.CharField(max_length=60)
    fabricacion=models.DateField
    
    def __str__(self) :
        return self.marca    
    

    