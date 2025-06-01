from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

def split_data(dataset_final):
    X = dataset_final.drop(columns=['average_rating', 'rating_difference'])
    y = dataset_final['average_rating']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test

def normalize_features(X_train, X_test):
    continuous_columns = ['rating_difference', 'Eco', 'Num_Moves', 'Avg_Move_Length']
    scaler = StandardScaler()
    X_train[continuous_columns] = scaler.fit_transform(X_train[continuous_columns])
    X_test[continuous_columns] = scaler.transform(X_test[continuous_columns])

    return X_train, X_test
