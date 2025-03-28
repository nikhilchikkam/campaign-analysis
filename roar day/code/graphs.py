import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'C:/Users/nxcstu/PycharmProjects/campaign_analysis/roar day/data/roar_day_performance_report.xlsx'
new_data = pd.read_excel(file_path)

# Plot for Open Rate of each message
plt.figure(figsize=(12, 10))

# Open Rate vs Message Name
plt.bar(new_data['Message_Name'], new_data['Open_Rate'], color='lightgreen')
plt.xlabel('Message Name')
plt.ylabel('Open Rate (%)')
plt.title('Open Rate for Each Message')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Plot for Opt Outs (Unsubscribe Count) of each message
plt.figure(figsize=(12, 10))

# Unsubscribe Count (Opt Outs) vs Message Name
plt.bar(new_data['Message_Name'], new_data['Unsubscribe_Count'], color='lightcoral')
plt.xlabel('Message Name')
plt.ylabel('Opt Outs (Unsubscribe Count)')
plt.title('Opt Outs (Unsubscribe Count) for Each Message')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Plot for Clickthrough Rate of each message
plt.figure(figsize=(12, 10))

# Clickthrough Rate vs Message Name
plt.bar(new_data['Message_Name'], new_data['Clickthrough_Rate'], color='lightblue')
plt.xlabel('Message Name')
plt.ylabel('Clickthrough Rate (%)')
plt.title('Clickthrough Rate for Each Message')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
