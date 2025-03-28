import pandas as pd

# Load the Excel file
file_path = 'C:/Users/nxcstu/PycharmProjects/campaign_analysis/founders_day/data/founders_day_clickthrough_details_report.xlsx'
data = pd.read_excel(file_path)

# Count the total occurrences of each URL for each message
url_count_per_message = data.groupby(['Message_Name', 'URL']).size().reset_index(name='Count')

# Sum the counts for each URL across different messages
url_total_count = url_count_per_message.groupby('URL')['Count'].sum().reset_index(name='Total Count')

# Merge with the original data to display each URL with its messages and counts
url_message_counts = url_count_per_message.merge(url_total_count, on='URL', how='left')

# Sort URLs by total count in descending order
url_total_count_sorted = url_total_count.sort_values(by='Total Count', ascending=False)

# Prepare the results in the requested format
result = []
for _, row in url_total_count_sorted.iterrows():
    result.append(f"{row['URL']}: {row['Total Count']}")
    message_data = url_message_counts[url_message_counts['URL'] == row['URL']]
    for _, message_row in message_data.iterrows():
        result.append(f"{message_row['Message_Name']}: {message_row['Count']}")
    result.append("")  # Add a line space after each URL and its messages

# Write the results to a text file
output_file = 'C:/Users/nxcstu/PycharmProjects/campaign_analysis/founders_day/results/founders_day_clickthrough_results.txt'
with open(output_file, 'w') as file:
    for line in result:
        file.write(f"{line}\n")

print(f"Results have been written to {output_file}")
