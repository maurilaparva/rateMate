from data_cleaning import load_and_clean_data, transform_categorical_features
from feature_engineering import feature_engineering
from model_training import split_data, normalize_features
from evaluation import evaluate_model
from sklearn.ensemble import RandomForestRegressor

file_path = "../club_games_data.csv"
dataset_cleaned = load_and_clean_data(file_path)
dataset_transformed = transform_categorical_features(dataset_cleaned)
dataset_with_features = feature_engineering(dataset_transformed)
X_train, X_test, y_train, y_test = split_data(dataset_with_features)
X_train, X_test = normalize_features(X_train, X_test)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
evaluate_model(y_test, y_pred)
