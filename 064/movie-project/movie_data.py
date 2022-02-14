import requests
import os


TMDB_API_KEY = os.environ["TMDB_API_KEY"]
TMDB_API_ENDPOINT = "https://api.themoviedb.org"
TMDB_API_SEARCH_ENDPOINT = f"{TMDB_API_ENDPOINT}/3/search/movie"
TMDB_API_MOVIE_ENDPOINT = f"{TMDB_API_ENDPOINT}/3/movie"


def search_movies(query):
    endpoint = TMDB_API_SEARCH_ENDPOINT
    params = {
        "api_key": TMDB_API_KEY,
        "query": query,
        "language": "en-US",
        "include_adult": "true"
    }

    r = requests.get(endpoint, params=params)

    movies = r.json().get("results")

    return movies


def get_movie_metadata(tmdb_movie_id):
    endpoint = f"{TMDB_API_MOVIE_ENDPOINT}/{tmdb_movie_id}"
    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US",
    }

    r = requests.get(endpoint, params=params)

    metadata = r.json()

    return metadata