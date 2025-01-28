import json
import pandas as pd

def load_spotify_data(file_paths):
    """Loads and combines Spotify streaming history from multiple JSON files."""
    data_frames = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            data_frames.append(pd.DataFrame(data))
    return pd.concat(data_frames, ignore_index=True)

def preprocess_data(df):
    """Preprocesses the data by converting timestamps and extracting key features."""
    df['endTime'] = pd.to_datetime(df['endTime'])
    df['year'] = df['endTime'].dt.year
    df['month'] = df['endTime'].dt.month
    df['hour'] = df['endTime'].dt.hour
    return df

def summarize_top_items(df, column, top_n=10):
    """Summarizes the top N items in a specified column (e.g., tracks or artists)."""
    return df[column].value_counts().head(top_n)
