# Higher or Lower - MyAnimeList ver (WIP) ⬆⬇
This is a simple web-based replica of the [Higher Lower Game](http://www.higherlowergame.com/), where you guess, which item has a bigger statistic. The original website compares Google searches from 2017, while this uses data from [MyAnimeList (MAL)](https://myanimelist.net/). MAL is an often used website for reviewing/rating/finding new Anime and Manga to watch. In this project, you'll have guess, which Anime/Manga has a higher average user score.

### How is the data retrieved?
All publicly available data can be fetched via MALs official API ([documentation](https://myanimelist.net/apiconfig/references/api/v2)). If you want to get up-to-date information yourself, you'll need an [account on MAL](https://myanimelist.net/register.php?from=%2F&) and [create a Client ID](https://myanimelist.net/apiconfig/create) for API access. The data-fetching implementation is currently hidden, but I'll potentially make it public in the future.

### How to install (Frontend-only)
Make sure you have [node.js](https://nodejs.org/en) installed with npm.
1. Run ```npm install``` inside the cloned repository.
2. Run ```npm start``` to run the app in development mode.
3. Open [http://localhost:3000](http://localhost:3000) in your Javascript-compatible Browser and navigate to the different projects at the top.

### State of the project
- most of the logic was formerly done with Django, but will now be re-implemented in the Frontend publicly
- a Backend may be added later to store complex information
- the Frontend will be hosted over Github Pages
