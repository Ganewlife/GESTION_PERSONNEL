from django.contrib import admin
from stagiaire_app.models import StagiaireInfo, Specialite, User

# Register your models here.
class StagiaireAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name','phone', 'birthday','emergency_phone','email')
admin.site.register(StagiaireInfo,StagiaireAdmin)

class SpecialiteAdmin(admin.ModelAdmin):
    list_display = ['nom']

admin.site.register(Specialite, SpecialiteAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'last_name', 'first_name', 'email', 'post']

admin.site.register(User, UserAdmin)