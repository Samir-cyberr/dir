import requests
import random

def get_genres(api_key):
    """Fetch available movie genres from TMDB API"""
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get('genres', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching genres: {e}")
        return []

def get_movies_by_genre(api_key, genre_id):
    """Fetch movies by genre from TMDB API"""
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get('results', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movies: {e}")
        return []

def display_movie_recommendation(movie):
    """Display movie information in a user-friendly format"""
    print("\n🎬 Recommended Movie:")
    print(f"📌 Title: {movie.get('title', 'Unknown')}")
    print(f"⭐ Rating: {movie.get('vote_average', 'N/A')}/10")
    print(f"📅 Release Date: {movie.get('release_date', 'Unknown')}")
    print(f"📝 Overview: {movie.get('overview', 'No description available')}")
    if movie.get('poster_path'):
        print(f"🖼️ Poster: https://image.tmdb.org/t/p/w500{movie['poster_path']}")

def main():
    # Replace with your TMDB API key
    API_KEY = "your_tmdb_api_key_here"
    
    # Get available genres
    genres = get_genres(API_KEY)
    if not genres:
        print("Failed to fetch genres. Please check your API key and internet connection.")
        return
    
    # Display genre menu
    print("🎥 Movie Genre Selector")
    for i, genre in enumerate(genres, 1):
        print(f"{i}. {genre['name']}")
    
    # Get user input
    try:
        choice = int(input("\nEnter the number of your preferred genre: "))
        if 1 <= choice <= len(genres):
            selected_genre = genres[choice-1]
            print(f"\nYou selected: {selected_genre['name']}")
            
            # Get movies from selected genre
            movies = get_movies_by_genre(API_KEY, selected_genre['id'])
            if movies:
                # Recommend a random movie
                recommended_movie = random.choice(movies)
                display_movie_recommendation(recommended_movie)
            else:
                print(f"No movies found in the {selected_genre['name']} genre.")
        else:
            print("Invalid selection. Please enter a number from the list.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()