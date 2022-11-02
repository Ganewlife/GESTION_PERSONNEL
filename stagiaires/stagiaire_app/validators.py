# on cree notre propre validateur de mot de passe de user puis on le remplace dans le fichiers setting
from django.core.exceptions import ValidationError


class ContainsLetterValidator:
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                'Le mot de passe doit contenir une lettre', code='password_no_letters')
                
    def get_help_text(self):
        return 'Votre mot de passe doit contenir au moins une lettre.'
    
class ContainsNumberValidator:
    def validate(self,password, user=None):
        if not  any(character.isdigit() for character in password):
            raise ValidationError(
                'Le mot de passe doit contenir un chiffre', code='password_no_number')
    
    def get_help_text(self):
        return 'Votre mot de passe doit contenir un chifre'
    
import re
class EmailValidator:
    def validate(self,email, user=None):
        if  re.search(r"^[A-Za-z0-9_!#$%&'*+\/=?]+@[A-Za-z0-9.-]+$", email):
            raise ValidationError(
                'Email invalide', code='amail_error')
    
    def get_help_text(self):
        return 'Votre adresse electronique doit etre valide '
        