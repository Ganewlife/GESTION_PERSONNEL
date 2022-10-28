from django.contrib import admin
from stagiaire_app.models import StagiaireInfo, User

# Register your models here.
class StagiaireAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name','phone', 'birthday','emergency_phone','email')
admin.site.register(StagiaireInfo,StagiaireAdmin)