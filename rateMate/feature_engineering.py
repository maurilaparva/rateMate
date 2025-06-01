import pandas as pd
import numpy as np

def extract_move(pgn):
    if(pgn.find('{[') == -1):
        original_list = pgn.split("\n")[-2].split()
        toberemoved_list = pgn.split("\n")[-2].split()[::3]
        new_list = [x for x in original_list if x not in toberemoved_list]
        return new_list
    else:
        return pgn.split("\n")[-2].split()[1::4]

def extract_move_features(moves):
    return {
        'Num_Moves': len(moves),
        'Avg_Move_Length': np.mean([len(move) for move in moves]),
    }

def feature_engineering(dataset_dropped):
    dataset_dropped['Moves'] = dataset_dropped['pgn'].apply(extract_move)
    move_features = dataset_dropped['Moves'].apply(extract_move_features).apply(pd.Series)
    for col in move_features.columns:
        dataset_dropped[col] = move_features[col]
    dataset_dropped['Avg_Move_Length'].fillna(0, inplace=True)

    return dataset_dropped
