# prelim_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the labeled data
def load_data(file_path):
    return pd.read_excel(file_path)


def data_summary(data):
    print("\n--- Data Summary ---")
    print("Shape of the DataFrame:", data.shape)
    print("\nColumn Information:")
    print(data.info())

    print("\nMissing Values:")
    print(data.isnull().sum())

    print("\nDescriptive Statistics:")
    print(data.describe(include='all'))


# 1. Count of each category (Bar Chart)
def category_counts(data):
    category_counts = data['Category'].value_counts()

    plt.figure(figsize=(10, 6))
    sns.barplot(x=category_counts.values, y=category_counts.index, palette='viridis')
    plt.xlabel('Count')
    plt.ylabel('Category')
    plt.title('Counts of Each Category')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


# 2. Hour of the day with highest click-through (Line Chart)
def hourly_clickthroughs(data):
    data['Hour'] = pd.to_datetime(data['Clickthrough__Date']).dt.hour
    hourly_counts = data['Hour'].value_counts().sort_index()

    plt.figure(figsize=(10, 6))
    sns.lineplot(x=hourly_counts.index, y=hourly_counts.values, marker='o', color='orange')
    plt.xlabel('Hour of Day')
    plt.ylabel('Click-Through Count')
    plt.title('Hourly Click-Throughs')
    plt.grid(True)
    plt.xticks(range(24))
    plt.tight_layout()
    plt.show()


# 3. Day of the week with highest click-through (Bar Chart)
def day_of_week_clickthroughs(data):
    data['DayOfWeek'] = pd.to_datetime(data['Clickthrough__Date']).dt.day_name()
    day_counts = data['DayOfWeek'].value_counts()[
        ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']]

    plt.figure(figsize=(10, 6))
    sns.barplot(x=day_counts.index, y=day_counts.values, palette='magma')
    plt.xlabel('Day of the Week')
    plt.ylabel('Click-Through Count')
    plt.title('Click-Throughs by Day of the Week')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# 4. Month of the year with highest click-through (Bar Chart)
def monthly_clickthroughs(data):
    data['Month'] = pd.to_datetime(data['Clickthrough__Date']).dt.month_name()
    month_counts = data['Month'].value_counts()[[
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]]

    plt.figure(figsize=(12, 6))
    sns.barplot(x=month_counts.index, y=month_counts.values, palette='cool')
    plt.xlabel('Month')
    plt.ylabel('Click-Through Count')
    plt.title('Click-Throughs by Month')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Main function to call all analysis functions
def main():
    file_path = r'data/AG_Report.xlsx'  # Change to your file path
    data = load_data(file_path)

    # print("data summary")
    # data_summary(data)
    #
    # print("Analyzing Category Counts...")
    # category_counts(data)
    #
    # print("Analyzing Hourly Click-Throughs...")
    # hourly_clickthroughs(data)

    print("Analyzing Day of the Week Click-Throughs...")
    day_of_week_clickthroughs(data)

    # print("Analyzing Monthly Click-Throughs...")
    # monthly_clickthroughs(data)


# Main guard
if __name__ == '__main__':
    main()
