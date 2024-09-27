import unittest
import pandas as pd
from movie_recommendation import recommend_movies

class TestMovieRecommendation(unittest.TestCase):
    def test_recommend_movies(self):
        user_data = {
            'User_ID': 1,
            'Watched_Genres': ['Action', 'Comedy'],
            'Favorite_Actors': ['Tom Hanks', 'Brad Pitt'],
        }
        movie_data = pd.DataFrame({
            'Movie_Name': ['Movie1', 'Movie2', 'Movie3'],
            'Genres': [['Action'], ['Comedy'], ['Drama']],
            'Actors': [['Tom Hanks'], ['Brad Pitt'], ['Leonardo DiCaprio']]
        })
        recommendations = recommend_movies(user_data, movie_data)
        self.assertIn('Movie1', recommendations)

if __name__ == '__main__':
    unittest.main()
