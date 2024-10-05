import json
from random import randint


# MyAnimeList API - anime_data.json syntax:
# {"data": [{"node": {"id": 123, "title": "Some Anime Name", ...}}, "node": {...}]}
# => dict -> array -> dict
# => anime_data["data"][ranking_index - 1]["node"]["title"] should get the the title of the anime with specified ranking_index



def get_anime_node(**kwargs) -> dict:
    """
    Looks up a specific entry from anime_data.json.
    
    :param int index: equals the rank of the anime on MyAnimeList (1-500)
    """
    index = kwargs.get("index", randint(1, 500))
    node = anime_data["data"][index-1]["node"]
    return node
        

def get_manga_node(**kwargs) -> dict:
    """
    Looks up a specific entry from manga_data.json
    
    :param int index: equals the rank of the manga on MyAnimeList (1-500)
    """
    index = kwargs.get("index", randint(1, 500))
    node = manga_data["data"][index-1]["node"]
    return node
    


# anime_data_json = open("data/anime_data.json")
# anime_data = json.load(anime_data_json)
# print(anime_data)


with open("data/anime_data.json") as f:
    anime_data = json.load(f)

with open("data/manga_data.json") as f:
    manga_data = json.load(f)


# example_anime1 = get_anime_node(index=1)
# example_anime2 = get_anime_node()
# print("Here's the first example anime:")
# print(example_anime1)
# print("Here's the second example anime:")
# print(example_anime2)