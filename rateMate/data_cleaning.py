import pandas as pd
import numpy as np

def load_and_clean_data(file_path):
    dataset = pd.read_csv(file_path)
    dataset_dropped = dataset.drop(labels=["white_username", "black_username", "white_id", "black_id"], axis=1)
    dataset_dropped['average_rating'] = (dataset_dropped['white_rating'] + dataset_dropped['black_rating']) / 2
    dataset_dropped['rating_difference'] = dataset_dropped['white_rating'] - dataset_dropped['black_rating']
    dataset_dropped = dataset_dropped.drop(labels=["white_rating", "black_rating", "black_result", "time_control"], axis=1)
    return dataset_dropped

def transform_categorical_features(dataset):
    from sklearn.preprocessing import LabelEncoder
    categorical_columns = ['white_result', 'time_class', 'rated', 'Eco']
    label_encoders = {col: LabelEncoder() for col in categorical_columns}
    for col in categorical_columns:
        dataset[col] = label_encoders[col].fit_transform(dataset[col])
    return dataset
