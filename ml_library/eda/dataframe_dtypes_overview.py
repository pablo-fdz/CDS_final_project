import pandas as pd

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