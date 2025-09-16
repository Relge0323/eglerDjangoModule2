from django.contrib import admin
from .models import Character, Ability, Quest, Equipment

# Register your models here.
@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'game', 'class_job', 'race')
    search_fields = ('name', 'game', 'class_job')
    filter_horizontal = ('abilities', 'quests')


@admin.register(Ability)
class AbilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'ability_type', 'element')
    search_fields = ('name', 'ability_type', 'element')


@admin.register(Quest)
class QuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty', 'reward')
    search_fields = ('name', 'difficulty', 'reward')


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'slot_type')
    filter_horizontal = ('characters',)