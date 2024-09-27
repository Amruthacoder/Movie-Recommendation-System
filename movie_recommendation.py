import pandas as pd

def recommend_movies(user_data, movie_data):
    watched_genres = user_data['Watched_Genres']
    favorite_actors = user_data['Favorite_Actors']
    
    # Debug: Print the columns in movie_data
    print("Columns in movie_data:", movie_data.columns)

    # Filter movies based on genres (make sure the column name matches)
    genre_filtered_movies = movie_data[movie_data['Genres'].apply(lambda x: any(genre in x for genre in watched_genres))]
    
    # Further filter movies based on favorite actors (make sure the column name matches)
    actor_filtered_movies = genre_filtered_movies[genre_filtered_movies['Actors'].apply(lambda x: any(actor in x for actor in favorite_actors))]
    
    return actor_filtered_movies['Movie_Name'].tolist()

# Load movie dataset
movie_data = pd.read_csv('data/movie.csv')

# Print the first few rows of the dataset for inspection
print(movie_data.head())

# Example user data
user_data = {
    'User_ID': 1,
    'Watched_Genres': ['Action', 'Comedy'],
    'Favorite_Actors': ['Tom Hanks', 'Brad Pitt']
}

# Call the function with user data and movie dataset
recommended_movies = recommend_movies(user_data, movie_data)

# Output the recommended movies
print("Recommended Movies:", recommended_movies)
