from django.shortcuts import render, get_object_or_404
from .models import Character

# Create your views here.
def character_list(request):
    characters = Character.objects.all()
    return render(request, 'rpg/character_list.html', {'characters': characters})


def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)
    return render(request, 'rpg/character_detail.html', {'character': character})