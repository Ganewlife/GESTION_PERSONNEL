from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label='Nom d\'utilisateur')
    #email = forms.EmailField(max_length=63, label='Email :')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'post')
        help_texts={
            'username' : None,
            'password' : None,
            'password2' : None,
        }

class SpecialiteForm(forms.ModelForm):
    class Metal: 
        model = models.Specialite
        fields = '__all__'

""" class CvForm(forms.ModelForm):
    class Meta:
        model = models.Cv
        fields = ['cv', 'title']

class DiplomeForm(forms.ModelForm):
    class Meta:
        model = models.Diplome
        fields = ['diplome', 'title']

class AttestationForm(forms.ModelForm):
    class Meta:
        model = models.Attestation
        fields = ['attestation', 'title' ]"""

class StagiaireForm(forms.ModelForm):
    edit_stagiaire = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = models.StagiaireInfo
        fields = '__all__'

class DeleteStagiaireForm(forms.Form):
    delete_stagiaire = forms.BooleanField(widget=forms.HiddenInput, initial=True)