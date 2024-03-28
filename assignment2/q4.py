# 28-march-2024
# CSC461 – Assignment2 – IDS – Data Visualization
# Ahmed Mazher
# FA20-BSE046
# The nuclear waste dataset contains the locations of several nuclear waste storage sites in the US. Use map of the US to show these sites as markers on the map. Clicking on a marker should display the name of the site. Pick the appropriate location, zoom level and images tiles for the map.


import folium
import pandas as pd

# Read the data
df = pd.read_csv('./sample_data/nuclear_waste_sites.csv')

# Create a map centered on the United States
us_map = folium.Map(location=[39.8283, -98.5795], zoom_start=4, tiles='OpenStreetMap')

# Add CircleMarkers for each nuclear waste site
for index, row in df.iterrows():
    folium.CircleMarker(
        location=[row['lat'], row['lon']],  # Coordinates
        radius=5,  # Marker radius
        color='red',  # Marker color
        fill=True,
        fill_color='red',
        fill_opacity=0.6,
        popup=row['text'],  # Popup text
    ).add_to(us_map)

# Display the map
us_map
