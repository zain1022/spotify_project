import os
import matplotlib.pyplot as plt
import seaborn as sns
from helper_functions import load_spotify_data, preprocess_data, summarize_top_items

# Define paths
data_dir = "./data"
output_dir = "./outputs"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Load data
file_paths = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith('.json')]
data = load_spotify_data(file_paths)

# Preprocess data
data = preprocess_data(data)

# Top Songs
top_songs = summarize_top_items(data, 'trackName')
print("Top Songs:")
print(top_songs)

# Top Artists
top_artists = summarize_top_items(data, 'artistName')
print("\nTop Artists:")
print(top_artists)

# Plot listening trends over time
plt.figure(figsize=(10, 6))
sns.histplot(data['endTime'].dt.date, bins=50, kde=False)
plt.title("Listening Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Streams")
plt.savefig(os.path.join(output_dir, "listening_trends.png"))
plt.close()

# Save summaries
top_songs.to_csv(os.path.join(output_dir, "top_songs.csv"))
top_artists.to_csv(os.path.join(output_dir, "top_artists.csv"))
