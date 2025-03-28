import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = "data/AnnualGivingWeekdayAnalysis_0324to0325_srbuadv.xlsx"  # Update with the correct file path
xls = pd.ExcelFile(file_path)

# Load the data from the first sheet
df = xls.parse(xls.sheet_names[0])

# Convert 'Email Date' to datetime format
df['Email Date'] = pd.to_datetime(df['Email Date'])

# Fill the 'Email Weekday' column with the corresponding weekday name
df['Email Weekday'] = df['Email Date'].dt.day_name()

# Calculate the average open rate and clickthrough rate per weekday
avg_rates = df.groupby('Email Weekday')[['Open_Rate', 'Clickthrough_Rate']].mean().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
)

# Create bar charts for Open Rate and Clickthrough Rate
plt.figure(figsize=(12, 5))

# Open Rate
plt.subplot(1, 2, 1)
plt.bar(avg_rates.index, avg_rates['Open_Rate'])
plt.xlabel('Weekday')
plt.ylabel('Average Open Rate (%)')
plt.title('Average Open Rate by Weekday')
plt.xticks(rotation=45)

# Clickthrough Rate
plt.subplot(1, 2, 2)
plt.bar(avg_rates.index, avg_rates['Clickthrough_Rate'])
plt.xlabel('Weekday')
plt.ylabel('Average Clickthrough Rate (%)')
plt.title('Average Clickthrough Rate by Weekday')
plt.xticks(rotation=45)

# Show the plots
plt.tight_layout()
plt.show()

# Save the updated DataFrame to a new Excel file
df.to_excel("updated_file.xlsx", index=False)
