from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# table des administrateurs

class User(AbstractUser):
    last_name = models.fields.CharField(max_length=50)
    first_name = models.fields.CharField(max_length=70)
    post = models.fields.CharField(max_length=20)
    password = models.fields.CharField(max_length=10)
    email = models.fields.EmailField(max_length=100)

# table des spécialités

class Specialite(models.Model):
    nom = models.fields.CharField(max_length=30)

# table des stagiaires

class StagiaireInfo(models.Model):
    last_name = models.fields.CharField(max_length=50) # nom
    first_name = models.fields.CharField(max_length=70) # prénom
    birthday = models.fields.DateField() # la date de naissance
    phone = models.fields.CharField(max_length=10) # le numéro de téléphone
    emergency_phone = models.fields.CharField(max_length=10) # le numéro de téléphone en cas d'urgence
    email = models.fields.EmailField(max_length=100) # l'adresse mail
    specialite = models.ForeignKey(Specialite, on_delete=models.CASCADE) # la spécialité (clé étrangère venant de la table Specialite)
    cv = models.fields.CharField(max_length=50) # le cv (un fichier)
    diplome = models.fields.CharField(max_length=50) # le diplôme (un fichier)
    attestation = models.fields.CharField(max_length=50) # l'attestation (un fichier)
    is_viewed = models.fields.BooleanField(default=False) # le marqueur de vu ou pas (par défaut à false ctd non lu)