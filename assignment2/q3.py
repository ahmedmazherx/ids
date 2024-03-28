# 28-march-2024
# CSC461 – Assignment2 – IDS – Data Visualization
# Ahmed Mazher
# FA20-BSE046
# Plot the relationship between ‘carat’ and ‘price’ of diamonds using a chart. Because it’s a large dataset, just plot the diamonds with a ‘clarify’ = ‘SI2’ and ‘color’ = ‘E’. Use the values of the ‘cut’ for colors in the plot.


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./sample_data/diamonds.csv')

# Filter the DataFrame
filtered_df = df[(df['clarity'] == 'SI2') & (df['color'] == 'E')]

# Define markers for different cuts
cut_markers = {'Fair': 's', 'Good': 'o', 'Very Good': '^', 'Premium': 'D', 'Ideal': 'x'}

plt.figure(figsize=(10, 6))  # Set the figure size for better readability

# Plot each cut separately with a different marker
for cut, marker in cut_markers.items():
    cut_data = filtered_df[filtered_df['cut'] == cut]
    plt.scatter(cut_data['carat'], cut_data['price'], marker=marker, label=cut)

plt.title('Relationship Between Carat and Price for SI2 Clarity and E Color Diamonds', fontsize=14)
plt.xlabel('Carat', fontsize=12)
plt.ylabel('Price (USD)', fontsize=12)
plt.legend(title='Cut', title_fontsize='13', labelspacing=1.2)
plt.tight_layout()  # Adjust the layout to make room for the legend and axis labels
plt.show()
