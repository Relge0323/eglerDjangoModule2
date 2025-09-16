from django.contrib import admin
from .models import Character

# Register your models here.
@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'game', 'class_job', 'race')
    search_fields = ('name', 'game', 'class_job')