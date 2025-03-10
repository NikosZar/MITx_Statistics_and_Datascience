import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
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

# Step 2: Run t-SNE with perplexity=30 on the PCA-reduced data
tsne = TSNE(n_components=2, perplexity=30, random_state=42)
log2_x_tsne = tsne.fit_transform(log2_x_pca)

# Create a scatterplot of the t-SNE result
plt.figure(figsize=(10, 8))
plt.scatter(log2_x_tsne[:, 0], log2_x_tsne[:, 1], c=y, cmap='viridis', alpha=0.7)
plt.colorbar(label='Class')
plt.xlabel('First t-SNE Dimension')
plt.ylabel('Second t-SNE Dimension')
plt.title('t-SNE of Log2-Transformed Data (PCA → t-SNE pipeline)')
plt.grid(True, alpha=0.3)
plt.show()