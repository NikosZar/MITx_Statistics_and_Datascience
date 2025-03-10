import numpy as np

# Load the data from p2 directory
x = np.load('/Users/nikos/Documents/GitHub/MITx_Statistics_and_Datascience/6.419x - Data Analysis Statistical Modeling and Computation in Applications/modules/module_2/data/p2_unsupervised/X.npy')
x_log2 = np.log2(x+1)

# the max value of the first column
max_val = x_log2[:,0].max()

print("Shape of X:", x_log2.shape)
print("Max value of X:", max_val)

from sklearn.decomposition import PCA
from sklearn.manifold import MDS, TSNE
import matplotlib.pyplot as plt

# Apply PCA
pca = PCA(n_components=2)
x_pca = pca.fit_transform(x)

# Create PCA plot
plt.figure(figsize=(10, 8))
plt.scatter(x_pca[:, 0], x_pca[:, 1], alpha=0.7)
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.title('PCA of Log2-Transformed Data')
plt.grid(True, alpha=0.3)
plt.show()

print(f"Variance explained by first two PCs: {sum(pca.explained_variance_ratio_):.4f}")

# Apply MDS
mds = MDS(n_components=2, random_state=42)
x_mds = mds.fit_transform(x)

# Create MDS plot
plt.figure(figsize=(10, 8))
plt.scatter(x_mds[:, 0], x_mds[:, 1], alpha=0.7)
plt.xlabel('First MDS Dimension')
plt.ylabel('Second MDS Dimension')
plt.title('MDS of Log2-Transformed Data')
plt.grid(True, alpha=0.3)
plt.show()

print(f"MDS Stress: {mds.stress_:.4f}")

# First reduce dimensionality with PCA for t-SNE
pca_50 = PCA(n_components=50)
x_pca_50 = pca_50.fit_transform(x)

# Apply t-SNE
tsne = TSNE(n_components=2, perplexity=30, random_state=42)
x_tsne = tsne.fit_transform(x_pca_50)

# Create t-SNE plot
plt.figure(figsize=(10, 8))
plt.scatter(x_tsne[:, 0], x_tsne[:, 1], alpha=0.7)
plt.xlabel('First t-SNE Dimension')
plt.ylabel('Second t-SNE Dimension')
plt.title('t-SNE of Log2-Transformed Data (PCA → t-SNE pipeline)')
plt.grid(True, alpha=0.3)
plt.show()
