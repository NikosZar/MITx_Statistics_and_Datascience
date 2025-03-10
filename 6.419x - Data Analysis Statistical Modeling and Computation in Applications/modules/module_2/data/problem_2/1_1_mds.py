import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import MDS
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import os

# Load the data using the absolute path
x = np.load('/Users/nikos/Documents/GitHub/MITx_Statistics_and_Datascience/6.419x - Data Analysis Statistical Modeling and Computation in Applications/modules/module_2/data/p2_unsupervised/X.npy')

# Create log2 transformed data
x_log2 = np.log2(x + 1)

print("Shape of X:", x_log2.shape)

# Step 1: Project onto top 50 PCs to reduce dimensionality before MDS
pca = PCA(n_components=50)
x_pca = pca.fit_transform(x_log2)

print(f"Variance explained by top 50 PCs: {sum(pca.explained_variance_ratio_):.4f}")

# Step 2: Run K-means on the PCA-reduced data with k=3 (for the three main cell types)
n_clusters = 3
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
cluster_labels = kmeans.fit_predict(x_pca)

# Step 3: Apply MDS to the PCA-reduced data
# Note: MDS preserves distances, showing how different the cell types are
mds = MDS(n_components=2,
          n_init=1,
          max_iter=300,
          random_state=42)
x_mds = mds.fit_transform(x_pca)

print(f"MDS stress: {mds.stress_:.2f}")

# Create visualization
plt.figure(figsize=(12, 10))

# Use distinct colors for the three clusters
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # Blue, Orange, Green
for i in range(n_clusters):
    plt.scatter(x_mds[cluster_labels == i, 0], x_mds[cluster_labels == i, 1],
               color=colors[i],
               alpha=0.7,
               s=50,
               label=f'Cell Type {i+1}')

plt.xlabel('MDS Dimension 1', fontsize=14)
plt.ylabel('MDS Dimension 2', fontsize=14)
plt.title('Three Main Brain Cell Types (MDS)', fontsize=16)
plt.legend(fontsize=12)
plt.grid(False)  # Remove grid for cleaner look

plt.tight_layout()
plt.savefig('images/brain_cell_types_mds.png', dpi=300)
plt.show()