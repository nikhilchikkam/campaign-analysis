import pandas as pd

# Load the datasets
tt_data = pd.read_excel('data/tt_data_cleaned.xlsx')
links_categories = pd.read_excel('data/links_categories.xlsx')

# Merge the datasets on the 'URL' column to assign labels
merged_data = pd.merge(tt_data, links_categories[['URL', 'Category']], on='URL', how='left')

# Save the labeled dataset to a new Excel file
merged_data.to_excel('data/labeled_tt_data.xlsx', index=False)

print("Labels have been assigned and saved to labeled_tt_data.xlsx")
