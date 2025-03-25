# category_engagement.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the labeled data
def load_data(file_path):
    return pd.read_excel(file_path)


# Category Engagement Analysis
def category_engagement(data):
    # Click-Through Rate (CTR) by Category
    category_ctr = data['Category'].value_counts(normalize=True) * 100

    plt.figure(figsize=(12, 6))
    sns.barplot(x=category_ctr.index, y=category_ctr.values, palette='Spectral')
    plt.xlabel('Category')
    plt.ylabel('Click-Through Rate (%)')
    plt.title('Click-Through Rate by Category')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Average Clicks per User per Category
    clicks_per_user = data.groupby(['cons_id', 'Category']).size().reset_index(name='Clicks')
    avg_clicks_per_category = clicks_per_user.groupby('Category')['Clicks'].mean()

    plt.figure(figsize=(12, 6))
    sns.barplot(x=avg_clicks_per_category.index, y=avg_clicks_per_category.values, palette='coolwarm')
    plt.xlabel('Category')
    plt.ylabel('Average Clicks per User')
    plt.title('Average Clicks per User per Category')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# Main function to call analysis function
def main():
    file_path = 'data/labeled_tt_data.xlsx'  # Change to your file path
    data = load_data(file_path)

    print("\nAnalyzing Category Engagement...")
    category_engagement(data)


# Main guard
if __name__ == '__main__':
    main()
