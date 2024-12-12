import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Now, we get a better visualization of the data types of the dataset
def dataframe_dtypes_overview(df):

    """
    Provides an overview of the data types in a DataFrame, including counts and variable names.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame.
    
    Returns:
    None: Prints the data type counts and variable names grouped by type.
    """

    dtype_counts = df.dtypes.value_counts()
    print("Data Type Overview:")
    for dtype, count in dtype_counts.items():
        print(f"\nData type: {dtype} ({count} variables)")
        cols = df.select_dtypes(include=[dtype]).columns
        print("Variables:", ", ".join(cols))

# We create a function that checks outliers

def check_outliers(dataframe):

    # Dictionary to hold the outliers information
    outliers_dict = {}

    for column in list(dataframe.columns):

        # For now, we ignore null values by dropping all observations with null values
        series_no_na = dataframe[column].dropna()

        # Calculate quartiles 25% and 75%
        q25, q75 = np.quantile(series_no_na, 0.25), np.quantile(series_no_na, 0.75)

        # Calculate the IQR
        iqr = q75 - q25

        # Calculate the outlier cutoff (in this case, set at 1.5 times the IQR)
        cut_off = iqr * 1.5

        # Calculate the lower and upper bound value
        lower, upper = q25 - cut_off, q75 + cut_off

        # Find the outliers
        outliers = [x for x in series_no_na if (x >= upper) or (x <= lower)]

        # Store the information in a dictionary, where each column will have its
        # own dictionary
        outliers_dict[column] = {
            'IQR': iqr,
            'Minimum': series_no_na.min(),
            'Lower Bound': lower,
            'Median': series_no_na.median(),
            'Upper Bound': upper,
            'Maximum': series_no_na.max(),
            'Outliers': outliers,
            'Num Outliers': len(outliers),
            'Num Observations': series_no_na.shape[0],
            'Percentage Outliers': (len(outliers) * 100)/series_no_na.shape[0]
        }

        # We convert the dictionary into a pandas DataFrame
        df_outliers = pd.DataFrame(outliers_dict)

    return df_outliers


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

# Loop for printing boxplots of numerical variables against the target (should
# be adapted to a function)

for feature in numerical_features:
    plt.figure(figsize=(20, 6))  # Adjust the figure size as needed
    sns.boxplot(data = df_tr, x='position_grouped', y=feature, hue = 'position_grouped', palette="Set2", legend=False)
    plt.title(f'Boxplot of {feature} by position', fontsize=14)
    plt.xlabel('Position', fontsize=12)
    plt.ylabel(feature, fontsize=12)
    plt.xticks(rotation=45)  # Rotate x-axis labels if needed
    plt.tight_layout()
    plt.show()

# Loop for showing barplots of categorical variables (should be adapted to a function)
for column in barplot_features:
    # We save the relative frequencies of each column
    relative_freq = df_tr[column].value_counts(normalize=True).reset_index()
    # We change the naming of the columns
    relative_freq.columns = ['Category', 'Relative Frequency']
    
    # Create a bar plot with Plotly
    fig = px.bar(relative_freq, x='Category', y='Relative Frequency',
                 title=f'Relative Frequency Barplot of the variable {column}')
    
    # Show the plot
    fig.show() 