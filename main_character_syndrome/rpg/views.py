from django.shortcuts import render
from .models import Character

# Create your views here.
def character_list(request):
    characters = Character.objects.all()
    return render(request, 'rpg/character_list.html', {'characters': characters})