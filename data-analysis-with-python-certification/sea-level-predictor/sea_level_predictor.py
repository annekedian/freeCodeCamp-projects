import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df.Year, df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_line = np.array([min(df['Year']), 2050])
    y_line = intercept + slope * x_line
    plt.plot(x_line, y_line, color = 'r', label='Line of Best Fit')

    # Create second line of best fit
    df2000 = df[df['Year'] >= 2000]
    slope, intercept, _, _, _ = linregress(df2000['Year'], df2000['CSIRO Adjusted Sea Level'])
    x_line = np.array([min(df2000['Year']), 2050])
    y_line = intercept + slope * x_line
    plt.plot(x_line, y_line, color = 'orange',label='Second Line of Best Fit')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()