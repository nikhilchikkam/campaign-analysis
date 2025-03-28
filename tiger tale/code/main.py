import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the labeled data
def load_data(file_path):
    return pd.read_excel(file_path)

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

def thursday_hourly_clickthroughs(data):
    # Convert the date column to datetime format
    data['DateTime'] = pd.to_datetime(data['Clickthrough__Date'])

    # Filter data for Thursday only
    thursday_data = data[data['DateTime'].dt.day_name() == 'Tuesday']

    # Get the count of click-throughs per hour on Thursday
    hourly_counts = thursday_data['DateTime'].dt.hour.value_counts().sort_index()

    # Plot the results
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=hourly_counts.index, y=hourly_counts.values, marker='o', color='blue')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Click-Through Count')
    plt.title('Hourly Click-Throughs on Tuesday')
    plt.grid(True)
    plt.xticks(range(24))
    plt.tight_layout()
    plt.show()

def main():
    file_path = r'tiger tale/data/AG_Report.xlsx'  # Change to your file path
    data = load_data(file_path)

    # print("Analyzing Day of the Week Click-Throughs...")
    # day_of_week_clickthroughs(data)
    #
    # print("Analyzing Hourly Click-Throughs...")
    # hourly_clickthroughs(data)

    print("Analyzing Hourly Click-Throughs on Thursday...")
    thursday_hourly_clickthroughs(data)


# Main guard
if __name__ == '__main__':
    main()