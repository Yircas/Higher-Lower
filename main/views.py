from django.shortcuts import render
from data.utils import get_anime_node, get_manga_node

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def random_anime(request):
    """
    Displays a random entry from anime_data.json. This is mainly for testing purposes.
    """
    anime_data = get_anime_node()
    return render(request, 'random_anime.html', anime_data)