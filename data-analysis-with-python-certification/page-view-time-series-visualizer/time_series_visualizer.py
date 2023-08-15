import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates = ['date'], index_col = 'date')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot

    fig, ax = plt.subplots(figsize=(15,5))
    
    ax = sns.lineplot(data = df, legend="brief", color = 'red')
    ax.set(title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set(xlabel = "Date", ylabel = "Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['month'] = df_bar['date'].dt.strftime('%B')
    df_bar['month_number'] = df_bar['date'].dt.month
    df_bar.sort_values(by=['month_number'], ascending=True, inplace = True)
    df_bar['year'] = df_bar['date'].dt.year

    # Draw bar plot

    fig, ax = plt.subplots(figsize=(10,8))
    ax = sns.barplot(data=df_bar, x="year", y="value", hue="month", errorbar = None)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    ax.legend(loc='upper left')
    ax.set(xlabel = "Years", ylabel = "Average Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['month_number'] = df_box['date'].dt.month
    df_box.sort_values(by=['month_number'], ascending=True, inplace = True)

    # Draw box plots (using Seaborn)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Boxplot 1
    sns.boxplot(data=df_box, x='year', y='value', ax=ax1)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax1.set_title('Year-wise Box Plot (Trend)')

    # Boxplot 2
    sns.boxplot(data=df_box, x='month', y='value', ax=ax2)
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.set_title('Month-wise Box Plot (Seasonality)')

    # Adjust spacing between subplots
    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
