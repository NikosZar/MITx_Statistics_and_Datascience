import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE, MDS
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
log2_x_pca = pca.fit_transform(x)

print(f"Variance explained by top 50 PCs: {sum(pca.explained_variance_ratio_):.4f}")

# Step 2: Run K-means on the PCA-reduced data
# Based on t-SNE visualization, let's use 5 clusters (adjust this number based on your t-SNE plot)
n_clusters = 5
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
cluster_labels = kmeans.fit_predict(log2_x_pca)

# Step 3: Visualize with PCA (2 components)
pca_viz = PCA(n_components=2)
log2_x_pca_viz = pca_viz.fit_transform(x)

plt.figure(figsize=(10, 8))
plt.scatter(log2_x_pca_viz[:, 0], log2_x_pca_viz[:, 1], c=cluster_labels, cmap='tab10', alpha=0.7)
plt.colorbar(label='Cluster')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.title('PCA with K-means Clusters')
plt.grid(True, alpha=0.3)
plt.show()

# Step 4: Visualize with MDS
mds = MDS(n_components=2, random_state=42)
log2_x_mds = mds.fit_transform(x)

plt.figure(figsize=(10, 8))
plt.scatter(log2_x_mds[:, 0], log2_x_mds[:, 1], c=cluster_labels, cmap='tab10', alpha=0.7)
plt.colorbar(label='Cluster')
plt.xlabel('First MDS Dimension')
plt.ylabel('Second MDS Dimension')
plt.title('MDS with K-means Clusters')
plt.grid(True, alpha=0.3)
plt.show()

# Step 5: Visualize with t-SNE
tsne = TSNE(n_components=2, perplexity=30, random_state=42)
log2_x_tsne = tsne.fit_transform(log2_x_pca)

plt.figure(figsize=(10, 8))
plt.scatter(log2_x_tsne[:, 0], log2_x_tsne[:, 1], c=cluster_labels, cmap='tab10', alpha=0.7)
plt.colorbar(label='Cluster')
plt.xlabel('First t-SNE Dimension')
plt.ylabel('Second t-SNE Dimension')
plt.title('t-SNE with K-means Clusters')
plt.grid(True, alpha=0.3)
plt.show()

# Optional: Compare with original class labels
plt.figure(figsize=(10, 8))
plt.scatter(log2_x_tsne[:, 0], log2_x_tsne[:, 1], c=y, cmap='viridis', alpha=0.7)
plt.colorbar(label='Original Class')
plt.xlabel('First t-SNE Dimension')
plt.ylabel('Second t-SNE Dimension')
plt.title('t-SNE with Original Classes')
plt.grid(True, alpha=0.3)
plt.show()