# content_based_filtering.py

import pandas as pd

def recommend_movies(user_data, movie_data):
    watched_genres = user_data['Watched_Genres']
    favorite_actors = user_data['Favorite_Actors']

    # Filter movies based on genres
    genre_filtered_movies = movie_data[movie_data['Watched_Genres'].apply(
        lambda x: any(genre in x for genre in watched_genres))]

    # Further filter movies based on favorite actors
    actor_filtered_movies = genre_filtered_movies[genre_filtered_movies['Favorite_Actors'].apply(
        lambda x: any(actor in x for actor in favorite_actors))]

    return actor_filtered_movies[['Movie_Name', 'Ratings']].sort_values(by='Ratings', ascending=False)

if __name__ == "__main__":
    # Example user data
    user_data = {
        'User_ID': 1,
        'Watched_Genres': ['Action', 'Comedy'],
        'Favorite_Actors': ['Actor A', 'Actor B'],
        'Ratings': None  # Not needed for recommendation
    }

    # Load the movie dataset
    movie_data = pd.read_csv('data/movie.csv')  # Adjust the path as necessary

    # Get recommendations
    recommendations = recommend_movies(user_data, movie_data)
    print("Recommended Movies:")
    print(recommendations)
