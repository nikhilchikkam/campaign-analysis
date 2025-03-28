import pandas as pd
import matplotlib.pyplot as plt

# Load Excel file
file_path = "data\Msg Performance.xlsx"  # Replace with your actual path
df = pd.read_excel(file_path, sheet_name='Sheet1')

# Convert 'Email Date' to datetime
df['Email Date'] = pd.to_datetime(df['Email Date'])

# Extract time-based features
df['Hour'] = df['Email Date'].dt.hour
df['Month'] = df['Email Date'].dt.month

# Grouping for analysis
grouped_weekday = df.groupby('Email Weekday')[['Open_Rate', 'Clickthrough_Rate']].mean()
grouped_hour = df.groupby('Hour')[['Open_Rate', 'Clickthrough_Rate']].mean()
grouped_month = df.groupby('Month')[['Open_Rate', 'Clickthrough_Rate']].mean()

# Sorting for visualization
grouped_weekday_sorted = grouped_weekday.sort_values(by='Open_Rate', ascending=False)
grouped_hour_sorted = grouped_hour.sort_index()
grouped_month_sorted = grouped_month.sort_index()

# Plot: Performance by Weekday
plt.figure(figsize=(10, 5))
plt.plot(grouped_weekday_sorted.index, grouped_weekday_sorted['Open_Rate'], marker='o', label='Open Rate')
plt.plot(grouped_weekday_sorted.index, grouped_weekday_sorted['Clickthrough_Rate'], marker='o', label='Clickthrough Rate')
plt.title('Average Performance by Weekday')
plt.xlabel('Weekday')
plt.ylabel('Rate (%)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot: Performance by Hour
plt.figure(figsize=(10, 5))
plt.plot(grouped_hour_sorted.index, grouped_hour_sorted['Open_Rate'], marker='o', label='Open Rate')
plt.plot(grouped_hour_sorted.index, grouped_hour_sorted['Clickthrough_Rate'], marker='o', label='Clickthrough Rate')
plt.title('Average Performance by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Rate (%)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot: Performance by Month
plt.figure(figsize=(10, 5))
plt.plot(grouped_month_sorted.index, grouped_month_sorted['Open_Rate'], marker='o', label='Open Rate')
plt.plot(grouped_month_sorted.index, grouped_month_sorted['Clickthrough_Rate'], marker='o', label='Clickthrough Rate')
plt.title('Average Performance by Month')
plt.xlabel('Month')
plt.ylabel('Rate (%)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
