import pandas as pd
import plotly.graph_objects as go

# Load the Excel file
file_path = 'C:/Users/nxcstu/PycharmProjects/campaign_analysis/roar day/data/roar_day_clickthrough_details_report.xlsx'
data = pd.read_excel(file_path)

# Count the total occurrences of each URL for each message
url_count_per_message = data.groupby(['Message_Name', 'URL']).size().reset_index(name='Count')

# Sum the counts for each URL across different messages
url_total_count = url_count_per_message.groupby('URL')['Count'].sum().reset_index(name='Total Count')

# Sort URLs by total count in descending order
url_total_count_sorted = url_total_count.sort_values(by='Total Count', ascending=False)

# Create the Bar chart with hyperlinks in the labels
fig = go.Figure()

# Add the bars
fig.add_trace(go.Bar(
    x=url_total_count_sorted['URL'],
    y=url_total_count_sorted['Total Count'],
    text=url_total_count_sorted['URL'],  # Show URLs as text on hover
    hovertemplate='<b>%{text}</b><br>Total Clickthrough Count: %{y}<extra></extra>',  # Add URL on hover
    marker=dict(color='skyblue')
))

# Update layout to make the plot look better
fig.update_layout(
    title='Total Clickthrough Count for Each URL',
    xaxis_title='URL',
    yaxis_title='Total Clickthrough Count',
    xaxis_tickangle=-45,
    showlegend=False,
)

# Show the plot
fig.show()

# Save the plot as an HTML file with clickable links
output_file = 'C:/Users/nxcstu/PycharmProjects/campaign_analysis/roar day/results/roar_day_clickthrough_results.html'
fig.write_html(output_file)

print(f"Interactive plot has been saved as {output_file}")
