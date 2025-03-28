# user_segmentation.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


# Load the labeled data
def load_data(file_path):
    data = pd.read_excel(file_path)
    # Drop rows where any of the demographic columns are empty
    data_cleaned = data.dropna(subset=['home_city', 'home_stateprov', 'home_zip', 'home_country'])
    print(f"Rows before cleaning: {data.shape[0]}")
    print(f"Rows after cleaning: {data_cleaned.shape[0]}")
    return data_cleaned


# User Segmentation and Behavior Analysis
def user_segmentation_behavior(data):
    # Demographic Analysis - Click-through patterns by location
    location_clicks = data['home_city'].value_counts().head(10)  # Top 10 cities

    plt.figure(figsize=(12, 6))
    sns.barplot(x=location_clicks.index, y=location_clicks.values, palette='cubehelix')
    plt.xlabel('City')
    plt.ylabel('Click-Through Count')
    plt.title('Top 10 Cities by Click-Through Count')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # User Clustering - Segment users based on click patterns
    user_clicks = data.groupby(['cons_id', 'Category']).size().unstack(fill_value=0)

    # Standardize the data
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(user_clicks)

    # Apply K-means clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(standardized_data)

    # Add cluster labels
    user_clicks['Cluster'] = clusters

    # Visualize Clusters using PCA
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(standardized_data)

    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(pca_result[:, 0], pca_result[:, 1], c=clusters, cmap='viridis', alpha=0.7)
    plt.title('User Segmentation (K-means Clustering)')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    plt.colorbar(scatter, label='Cluster')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    print("User Segmentation Analysis Complete. Cluster Centers:")
    print(kmeans.cluster_centers_)


# Main function to call analysis function
def main():
    file_path = 'data/labeled_tt_data.xlsx'  # Change to your file path
    data = load_data(file_path)

    print("\nAnalyzing User Segmentation and Behavior...")
    user_segmentation_behavior(data)


# Main guard
if __name__ == '__main__':
    main()
