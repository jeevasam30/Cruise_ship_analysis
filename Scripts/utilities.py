# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


# Function to load data
def load_data(file_path):
    '''para: path of your file in csv
    return: csv file is returned as dataframe'''
    return pd.read_csv(file_path) 

# Function to filter necessary columns
def filter_columns(data, necessary_columns):
    '''para : 1.The data in which you want to filter columns
              2.all the necessary columns in a list
    return: gives a filtered data
'''
    return data[necessary_columns]

# Function to handle missing values
def handle_missing_values(data):
    '''para: data for handling missing values
     return: data is returned where the missing values are filled with mean values '''
    numeric_columns = data.select_dtypes(include='number').columns
    means = data[numeric_columns].mean()
    data_filled = data.copy()
    data_filled[numeric_columns] = data_filled[numeric_columns].fillna(means)
    return data_filled

# Function to convert date columns
def convert_dates(data, date_columns):
    '''para: data and which are the date columns
    return : data retruned with data columns changed to datetime'''
    for col in date_columns:
        data[col] = pd.to_datetime(data[col])
    return data

# Function to clean data
def clean_data(data, necessary_columns, date_columns):
    """
    Clean the dataset by filtering columns, handling missing values, and converting date columns.
    
    Parameters:
    data : pd.DataFrame
        The input DataFrame.
    necessary_columns : list
        List of columns to keep.
    date_columns : list
        List of columns to convert to datetime.

    Returns:
    pd.DataFrame
        Cleaned DataFrame.
    """
    filtered_data = filter_columns(data, necessary_columns)
    data_filled = handle_missing_values(filtered_data)
    data_cleaned = convert_dates(data_filled, date_columns)
    return data_cleaned

# Function to plot missing values
def plot_missing_values(data, title):
    """
    Plot a bar chart of the number of missing values in each column.
    
    Parameters:
    data : pd.DataFrame
        The input DataFrame.
    title : str
        Title of the plot.
    """
    missing_values_count = data.isnull().sum()
    plt.figure(figsize=(12, 8))
    sns.barplot(x=missing_values_count.values, y=missing_values_count.index, palette='viridis')
    plt.title(title)
    plt.xlabel('Number of Missing Values')
    plt.ylabel('Column Names')
    plt.show()

# Function to plot histograms for numerical columns
def plot_histograms(data, title):
    """
    Plot histograms for all numerical columns in the DataFrame.
    
    Parameters:
    data : pd.DataFrame
        The input DataFrame.
    title : str
        Title of the plot.
    """
    numeric_columns = data.select_dtypes(include='number').columns
    data[numeric_columns].hist(figsize=(15, 15), bins=20, edgecolor='black')
    plt.suptitle(title)
    plt.show()

# Function to plot boxplots for numerical columns
def plot_boxplots(data, title):
    """
    Plot boxplots for all numerical columns in the DataFrame.
    
    Parameters:
    data : pd.DataFrame
        The input DataFrame.
    title : str
        Title of the plot.
    """
    numeric_columns = data.select_dtypes(include='number').columns
    plt.figure(figsize=(15, 15))
    for i, column in enumerate(numeric_columns, 1):
        plt.subplot(len(numeric_columns)//4 + 1, 4, i)
        sns.boxplot(y=data[column], palette='viridis')
        plt.title(column)
    plt.suptitle(title)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

# Function to plot correlation heatmap
def plot_correlation_heatmap(data, title):
    """
    Plot a heatmap of the correlation matrix for the DataFrame.
    
    Parameters:
    data : pd.DataFrame
        The input DataFrame.
    title : str
        Title of the plot.
    """
    plt.figure(figsize=(14, 12))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt='.1f', annot_kws={"size": 8})
    plt.title(title)
    plt.tight_layout()
    plt.show()