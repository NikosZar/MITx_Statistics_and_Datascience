import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

# Load the data from p1 directory
x = np.load(os.path.join(current_dir, 'p1', 'X.npy'))
y = np.load(os.path.join(current_dir, 'p1', 'y.npy'))

print("Shape of X:", x.shape)
print("Shape of y:", y.shape)

# Create log2 transformed data
log2_x = np.log2(x + 1)

# Step 1: Project onto top 50 PCs
pca = PCA(n_components=50)
log2_x_pca = pca.fit_transform(log2_x)

print(f"Variance explained by top 50 PCs: {sum(pca.explained_variance_ratio_):.4f}")

# Step 2: Run K-means with different numbers of clusters
max_clusters = 15
inertia_values = []

for k in range(1, max_clusters + 1):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(log2_x_pca)
    inertia_values.append(kmeans.inertia_)
    print(f"K={k}, Inertia={kmeans.inertia_:.2f}")

# Step 3: Plot the elbow curve
plt.figure(figsize=(10, 6))
plt.plot(range(1, max_clusters + 1), inertia_values, 'bo-')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia (Within-Cluster Sum of Squares)')
plt.title('Elbow Method for Optimal k')
plt.grid(True)
plt.show()

# Step 4: Based on the elbow plot, choose the optimal number of clusters
# Let's say we choose k=5 (you should adjust this based on your plot)
optimal_k = 5
kmeans_optimal = KMeans(n_clusters=optimal_k, random_state=42)
kmeans_optimal.fit(log2_x_pca)

print(f"\nChosen number of clusters: {optimal_k}")
print(f"Inertia at k={optimal_k}: {kmeans_optimal.inertia_:.2f}")