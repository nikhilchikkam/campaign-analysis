import pandas as pd

# Load the dataset
file_2 = r'C:\Users\nxcstu\PycharmProjects\campaign_analysis\roar_day_gls\data\RIT University Advancement Web Analytics GA4_Campaign Metrics_Table (1).csv'
data_2 = pd.read_csv(file_2)


# Clean the data to ensure columns are numeric and handle NaN values
def clean_data(data):
    # Remove percentage signs and convert Interaction Rate and CTA Click Rate to numeric
    columns_to_clean = ['Interaction Rate', 'CTA Click Rate']

    for col in columns_to_clean:
        data[col] = data[col].replace({',': '', '%': ''}, regex=True).astype(float)

    # Replace NaN values with 0 in the numeric columns
    data.fillna(0, inplace=True)

    # Convert other relevant columns to numeric (if needed)
    data['Total Users'] = pd.to_numeric(data['Total Users'], errors='coerce')
    data['Sessions'] = pd.to_numeric(data['Sessions'], errors='coerce')
    data['Sessions w/ Interaction'] = pd.to_numeric(data['Sessions w/ Interaction'], errors='coerce')

    return data


# Clean the dataset
data_2 = clean_data(data_2)


# Function to find top 10 URLs based on a given metric
def top_10_urls(data, metric):
    # Group by URL and aggregate the specified metric
    top_urls = data.groupby('Entrance/Landing Page')[metric].sum()

    # Sort the values in descending order and select the top 10
    top_urls_sorted = top_urls.sort_values(ascending=False).head(10)

    print(f"Top 10 URLs based on {metric}:")
    print(top_urls_sorted)


# Find top 10 URLs for each metric
metrics = ['Total Users', 'Sessions', 'Sessions w/ Interaction', 'Interaction Rate', 'CTA Click Rate']
for metric in metrics:
    top_10_urls(data_2, metric)
    print("\n")
