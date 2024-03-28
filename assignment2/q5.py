# 28-march-2024
# CSC461 – Assignment2 – IDS – Data Visualization
# Ahmed Mazher
# FA20-BSE-046
# The Pakistan heritage sites dataset contains the geo locations of a number of heritage sites across Pakistan. Show these sites as markers on a map of the Pakistan. Clicking on a marker should display the name of the site. Pick the appropriate location, zoom level and images tiles for the map.




import folium
import pandas as pd

# Load the data
df = pd.read_csv('./sample_data/pak-heritage-sites.csv', header=None)
df.columns = ['Latitude', 'Longitude', 'Site']

# Initialize a folium map centered around the geographic center of Pakistan
pakistan_map = folium.Map(location=[30.3753, 69.3451], zoom_start=6)

# Add CircleMarkers for each heritage site
for index, row in df.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],  # Coordinates
        radius=5,  # Marker radius
        color='blue',  # Marker color
        fill=True,
        fill_color='blue',
        fill_opacity=0.6,
        popup=row['Site'],  # Popup text
    ).add_to(pakistan_map)

# Display the map
pakistan_map
