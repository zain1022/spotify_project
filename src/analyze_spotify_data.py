import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load Spotify data
data_path = os.path.join('data', 'MyData', 'YourDataFile.csv')  # Update with actual file name
try:
    spotify_data = pd.read_csv(data_path)
except FileNotFoundError:
    raise Exception("Spotify data file not found. Please ensure it's in the correct location.")

# Data Analysis
def analyze_top_songs(data):
    top_songs = data['song_name'].value_counts().head(10)
    print("\nTop 10 Songs:")
    print(top_songs)
    return top_songs

def analyze_top_artists(data):
    top_artists = data['artist_name'].value_counts().head(10)
    print("\nTop 10 Artists:")
    print(top_artists)
    return top_artists

def analyze_genres(data):
    if 'genre' in data.columns:
        top_genres = data['genre'].value_counts().head(10)
        print("\nTop 10 Genres:")
        print(top_genres)
        return top_genres
    else:
        print("\nGenre data not available.")
        return None

# Visualization
def plot_top_songs(top_songs):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_songs.values, y=top_songs.index)
    plt.title("Top 10 Songs")
    plt.xlabel("Play Count")
    plt.ylabel("Songs")
    plt.tight_layout()
    plt.savefig(os.path.join('output', 'top_songs.png'))
    plt.show()

def plot_top_artists(top_artists):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_artists.values, y=top_artists.index)
    plt.title("Top 10 Artists")
    plt.xlabel("Play Count")
    plt.ylabel("Artists")
    plt.tight_layout()
    plt.savefig(os.path.join('output', 'top_artists.png'))
    plt.show()

def plot_top_genres(top_genres):
    if top_genres is not None:
        plt.figure(figsize=(10, 6))
        sns.barplot(x=top_genres.values, y=top_genres.index)
        plt.title("Top 10 Genres")
        plt.xlabel("Play Count")
        plt.ylabel("Genres")
        plt.tight_layout()
        plt.savefig(os.path.join('output', 'top_genres.png'))
        plt.show()

# Main execution
if __name__ == "__main__":
    print("Analyzing Spotify Data...")
    os.makedirs('output', exist_ok=True)

    top_songs = analyze_top_songs(spotify_data)
    top_artists = analyze_top_artists(spotify_data)
    top_genres = analyze_genres(spotify_data)

    plot_top_songs(top_songs)
    plot_top_artists(top_artists)
    plot_top_genres(top_genres)
