import numpy as np
from sklearn.manifold import MDS
from sklearn.metrics import pairwise_distances
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

# Apply MDS to the log2-transformed data
# Using Euclidean distance by default
mds = MDS(n_components=2, random_state=42)
log2_x_mds = mds.fit_transform(log2_x)

# Print the stress (goodness of fit)
print(f"MDS Stress: {mds.stress_:.4f}")

# Create a scatterplot of the MDS result
plt.figure(figsize=(10, 8))
plt.scatter(log2_x_mds[:, 0], log2_x_mds[:, 1], c=y, cmap='viridis', alpha=0.7)
plt.colorbar(label='Class')
plt.xlabel('First MDS Dimension')
plt.ylabel('Second MDS Dimension')
plt.title('MDS of Log2-Transformed Data')
plt.grid(True, alpha=0.3)
plt.show()

# Optional: Compare with custom distance matrix
# For example, using correlation distance
corr_dist = 1 - np.corrcoef(log2_x)
mds_corr = MDS(n_components=2, dissimilarity='precomputed', random_state=42)
log2_x_mds_corr = mds_corr.fit_transform(corr_dist)

# Plot the correlation-based MDS
plt.figure(figsize=(10, 8))
plt.scatter(log2_x_mds_corr[:, 0], log2_x_mds_corr[:, 1], c=y, cmap='viridis', alpha=0.7)
plt.colorbar(label='Class')
plt.xlabel('First MDS Dimension (Correlation)')
plt.ylabel('Second MDS Dimension (Correlation)')
plt.title('MDS with Correlation Distance')
plt.grid(True, alpha=0.3)
plt.show()