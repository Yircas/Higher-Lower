from django.shortcuts import render
from data.utils import get_anime_node, get_manga_node
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def random_anime(request):
    """
    Displays a random entry from anime_data.json. This is mainly for testing purposes.
    """
    anime_data = get_anime_node()
    return render(request, 'random_anime.html', anime_data)

def display(request, category):
    """
    Displays a random entry from a data category. This is mainly for testing purposes.
    """
    if category == "anime":
        data = get_anime_node()
        data["category"] = "anime"
    elif category == "manga":
        data = get_manga_node()
        data["category"] = "manga"
    else:
        messages.info(request, f'{category} is not a valid category!')
        return render(request, 'home.html', {})
    return render(request, 'display.html', data)