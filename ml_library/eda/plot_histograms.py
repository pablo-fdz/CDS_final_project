import pandas as np
import numpy as np
import matplotlib.pyplot as plt

# Plot histograms (should be adapted only for numerical variables)
def plot_histograms(dataframe, my_bins=10):
    num_columns = len(dataframe.columns)
    num_rows = (num_columns + 1) // 2  # Ensure enough rows for all subplots
    fig, axes = plt.subplots(num_rows, 2, figsize=(12, 4 * num_rows))  # Adjust figure size based on rows
    
    for i, column in enumerate(dataframe.columns):
        row, col = divmod(i, 2)  # Determine the position in the grid
        ax = axes[row, col] if num_rows > 1 else axes[col]  # Handle 1-row case
        ax.hist(dataframe[column], density=True, bins=my_bins)
        ax.set_xlabel(column)
        ax.set_ylabel('Density')
    
    fig.tight_layout()  # Automatically adjust subplot parameters to fit the figure
    plt.show()