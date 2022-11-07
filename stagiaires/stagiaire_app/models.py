from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

# table des administrateurs

class User(AbstractUser):
    post = models.fields.CharField(max_length=20)
    """ email = models.EmailField(unique=True)
    username = email
    USERNAME_FIELD = 'email'"""
    REQUIRED_FIELDS = ('email','first_name', 'last_name', 'post') 
# table des spécialités

class Specialite(models.Model):
    nom = models.fields.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nom

class StagiaireInfo(models.Model):
    last_name = models.CharField(max_length=50) # nom
    first_name = models.CharField(max_length=70) # prénom
    birthday = models.DateField() # la date de naissance
    phone = models.CharField(max_length=10) # le numéro de téléphone
    emergency_phone = models.CharField(max_length=10) # le numéro de téléphone en cas d'urgence
    email = models.EmailField(max_length=100) # l'adresse mail
    specialite = models.ForeignKey(Specialite, on_delete=models.CASCADE) # la spécialité (clé étrangère venant de la table Specialite)
    cv = models.FileField(max_length=50) # le cv (un fichier)
    diplome = models.FileField(max_length=50) # le diplôme (un fichier)
    attestation = models.FileField(max_length=50) # l'attestation (un fichier)
    created_at = models.DateTimeField(auto_now_add=True)

# table des stagiaires
""" class Cv(models.Model):
    cv = models.FileField()
    title = models.CharField(max_length=128, blank=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(models.FileField)

class Diplome(models.Model):
    diplome = models.FileField()
    title = models.CharField(max_length=128, blank=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

class Attestation(models.Model):
    attestation = models.FileField()
    title = models.CharField(max_length=128, blank=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True) """
    

""" class StagiaireInfo(models.Model):
    cv = models.ForeignKey(Cv, null=True, on_delete=models.SET_NULL, blank=True)
    diplome = models.ForeignKey(Diplome, null=True, on_delete=models.SET_NULL, blank=True)
    attestation = models.ForeignKey(Attestation, null=True, on_delete=models.SET_NULL, blank=True)
    last_name = models.fields.CharField(max_length=50) # nom
    first_name = models.fields.CharField(max_length=70) # prénom
    birthday = models.fields.DateField() # la date de naissance
    phone = models.fields.CharField(max_length=10) # le numéro de téléphone
    emergency_phone = models.fields.CharField(max_length=10) # le numéro de téléphone en cas d'urgence
    email = models.fields.EmailField(max_length=100)
    is_viewed = models.fields.BooleanField(default=False) # le marqueur de vu ou pas (par défaut à false ctd non lu)
    content = models.CharField(max_length=5000) """
    
