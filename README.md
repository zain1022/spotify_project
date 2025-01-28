# Spotify Data Analysis

## Project Description
This project analyzes Spotify user data to identify top songs, artists, and genres, as well as to highlight listening preferences. Graphs and visualizations are generated to clearly communicate patterns.

## Folder Structure
- `data/`: Contains the Spotify user data.
- `scripts/`: Source code for data analysis and visualization.
- `notebooks/`: (Optional) Jupyter notebooks for exploratory analysis.
- `output/`: Generated graphs and visualizations.
- `README.md`: Project documentation.


## Setup Instructions
1. Clone this repository.
2. Ensure Python 3.x is installed along with the following packages:
   - pandas
   - matplotlib
   - seaborn
   - json

3. Place your Spotify JSON files in the `data/` folder.

## Scripts
- `data_analysis.py`: Parses Spotify JSON files, analyzes the data, and generates visualizations.
- `helper_functions.py`: Contains helper functions for data cleaning and aggregation.

## Example Analysis
This project identifies:
- Top songs and artists.
- Listening trends by year and month.
- Genre preferences (if genre metadata is present).

## Output
Visualizations and results will be stored in the `outputs/` folder.

