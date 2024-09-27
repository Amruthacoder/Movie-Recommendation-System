# automl_model.py

import pandas as pd
from tpot import TPOTRegressor
from sklearn.model_selection import train_test_split

# Load the dataset
def load_data(file_path):
    return pd.read_csv(file_path)

# Train AutoML model
def train_automl_model(data):
    # Split the data into features and target
    X = data[['User_ID', 'Watched_Genres', 'Favorite_Actors']]  # Adjust based on your features
    y = data['Ratings']

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the AutoML model
    tpot = TPOTRegressor(verbosity=2, random_state=42)
    tpot.fit(X_train, y_train)

    # Evaluate the model
    print(tpot.score(X_test, y_test))

    # Export the pipeline
    tpot.export('best_pipeline.py')

if __name__ == "__main__":
    # Load your data
    data = load_data('data/movie.csv')  # Adjust the path as necessary
    train_automl_model(data)
