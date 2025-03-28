import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_1 = r'C:\Users\nxcstu\PycharmProjects\campaign_analysis\roar_day_gls\data\RIT University Advancement Web Analytics GA4_Campaign Metrics_Table.csv'
data_1 = pd.read_csv(file_1)


# Clean the data to ensure columns are numeric and handle NaN values
def clean_data(data):
    # Remove commas and convert columns to numeric
    columns_to_clean = ['Total Users', 'Sessions', 'Sessions w/ Interaction', 'Interaction Rate', 'CTA Click Rate']

    # Check and print the first few values of the columns before cleaning
    print("Before cleaning:")
    print(data[columns_to_clean].head())

    for col in columns_to_clean:
        # Remove percentage signs and convert to numeric
        if col in ['Interaction Rate', 'CTA Click Rate']:
            data[col] = data[col].replace({',': '', '%': ''}, regex=True).astype(float) / 100
        else:
            data[col] = pd.to_numeric(data[col].replace({',': ''}, regex=True), errors='coerce')

    # Check and print the first few values of the columns after cleaning
    print("After cleaning:")
    print(data[columns_to_clean].head())

    # Replace NaN values with 0 or another appropriate value
    data.fillna(0, inplace=True)
    return data


# Clean the dataset
data_1 = clean_data(data_1)


# Function to plot pie charts by Medium
def plot_pie_charts(data):
    metrics = ['Total Users', 'Sessions', 'Sessions w/ Interaction', 'Interaction Rate', 'CTA Click Rate']

    for metric in metrics:
        # Group by 'Medium' and sum the values for the metric
        metric_data = data.groupby('Medium')[metric].sum()

        # Drop NaN values if any, before plotting
        metric_data = metric_data.dropna()

        # Skip empty data (if all values are NaN or 0)
        if metric_data.empty or (metric_data.sum() == 0):
            print(f"Skipping {metric} pie chart due to insufficient data.")
            continue

        # Plot the pie chart
        plt.figure(figsize=(8, 6))
        plt.pie(metric_data, labels=metric_data.index, autopct='%1.1f%%', startangle=140)
        plt.title(f"Distribution of {metric} by Medium")
        plt.axis('equal')
        plt.show()

# Function to plot bar charts for average of each metric by medium
def plot_bar_chart(data):
    metrics = ['Total Users', 'Sessions', 'Sessions w/ Interaction', 'Interaction Rate', 'CTA Click Rate']

    avg_metrics = data.groupby('Medium')[metrics].mean()

    avg_metrics.plot(kind='bar', figsize=(10, 7))
    plt.title('Average Metrics by Medium')
    plt.ylabel('Average Values')
    plt.xlabel('Medium')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Function to compare interaction rates by content type
def plot_content_interaction_comparison(data):
    content_interaction = data.groupby('Content')['Interaction Rate'].mean()

    content_interaction.plot(kind='bar', figsize=(10, 7))
    plt.title('Interaction Rate Comparison by Content')
    plt.ylabel('Average Interaction Rate')
    plt.xlabel('Content')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Function to plot all charts in one screen
def plot_all_charts(data):
    fig, axs = plt.subplots(3, 2, figsize=(14, 12))

    # Pie charts for each metric
    metrics = ['Total Users', 'Sessions', 'Sessions w/ Interaction', 'Interaction Rate', 'CTA Click Rate']
    for i, metric in enumerate(metrics):
        ax = axs[i // 2, i % 2]
        metric_data = data.groupby('Medium')[metric].sum()
        metric_data = metric_data.dropna()

        if not metric_data.empty and metric_data.sum() != 0:
            ax.pie(metric_data, labels=metric_data.index, autopct='%1.1f%%', startangle=140)
            ax.set_title(f"Distribution of {metric} by Medium")
        else:
            ax.set_title(f"Skipping {metric} Pie Chart\nDue to Insufficient Data")
            ax.axis('off')

    # Plot campaign distribution by medium as a pie chart
    campaign_data = data.groupby('Medium')['Campaign'].nunique()
    campaign_data = campaign_data.dropna()

    ax = axs[2, 0]  # Last chart in the first row
    if not campaign_data.empty and campaign_data.sum() != 0:
        ax.pie(campaign_data, labels=campaign_data.index, autopct='%1.1f%%', startangle=140)
        ax.set_title("Distribution of Campaigns by Medium")
    else:
        ax.set_title("Skipping Campaign Distribution Pie Chart\nDue to Insufficient Data")
        ax.axis('off')

    # Bar chart for average metrics by medium
    avg_metrics = data.groupby('Medium')[metrics].mean()
    ax = axs[2, 1]  # Last chart in the second row
    avg_metrics.plot(kind='bar', ax=ax)
    ax.set_title('Average Metrics by Medium')
    ax.set_ylabel('Average Values')
    ax.set_xlabel('Medium')

    plt.tight_layout()
    plt.show()

# Run the function to plot all charts
plot_all_charts(data_1)
plot_bar_chart(data_1)
plot_content_interaction_comparison(data_1)
