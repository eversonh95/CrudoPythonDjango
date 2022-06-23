from django.db import models

# Create your models here.

#python manage.py makemigrations para criar as migrações com banco de dados
#python manage.py migrate para criar o banco de dados
class Carros(models.Model):
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()