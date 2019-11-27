from django.db import models

# Create your models here.
class Utilisateur(models.Model):
    mail = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    status = models.CharField (max_length=15)
    niveau = models.CharField(max_length=3)