# Higher or Lower - MyAnimeList ver (WIP) ⬆⬇
This is a simple web-based replica of the [Higher Lower Game](http://www.higherlowergame.com/), where you guess, which item has a bigger statistic. The original website compares Google searches from 2017, while this uses data from [MyAnimeList (MAL)](https://myanimelist.net/). MAL is an often used website for reviewing/rating/finding new Anime and Manga to watch. In this project, you'll have guess, which Anime/Manga has a higher average user score.

### How is the data retrieved?
All publicly available data can be fetched via MALs official free API ([documentation](https://myanimelist.net/apiconfig/references/api/v2)). If you want to get up-to-date information yourself, you'll need an [account on MAL](https://myanimelist.net/register.php?from=%2F&) and [create a Client ID](https://myanimelist.net/apiconfig/create) for API access.
- [/data/](https://github.com/Yircas/Higher-Lower/tree/main/data): contains retireved data from MAL and a [Jupyter Notebook](https://github.com/Yircas/Higher-Lower/tree/main/data/fetch_data.ipynb), if you want to fetch new data yourself.

### How do I use/install this?
To use this project on your own machine:
1. copy the repository with ```git clone https://github.com/Yircas/Higher-Lower.git```
2. make sure you have the pipenv package manager and Python +3.12, then run ```pipenv install``` in the project's directory
3. activate the virtual environment via ```pipenv shell```
4. retrieve the data with [this Jupyter Notebook](https://github.com/Yircas/Higher-Lower/tree/main/data/fetch_data.ipynb)
5. start the server with ```python manage.py runserver``` and open http://127.0.0.1:8000/ in your Browser
6. stare at a buggy, unfinished website, that I am currently still working on 🗿
I'm planning to deploy this with a (free) web-hosting service, so you can directly play it in your Browser without any setup. I'll put the link here, if the website's finished.