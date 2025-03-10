import numpy as np
from sklearn.decomposition import PCA
import os
import matplotlib.pyplot as plt

current_dir = os.path.dirname(os.path.abspath(__file__))

# Load the data from p1 directory
x = np.load(os.path.join(current_dir, 'p1', 'X.npy'))
y = np.load(os.path.join(current_dir, 'p1', 'y.npy'))

print("Shape of X:", x.shape)
print("Shape of y:", y.shape)

#the value of the largest entry in the first column


print(x[:,0].dtype)
max_val = x[:, 0].max()
print(max_val)

log2_val = np.log2(x + 1)
log2_max_val = log2_val[:, 0].max()
print("log_2 max value is:", log2_max_val)

# Compute PCA for raw data
pca_raw = PCA()
pca_raw.fit(x)
cum_var_raw = np.cumsum(pca_raw.explained_variance_ratio_)

# Compute PCA for log2 transformed data
log2_x = np.log2(x + 1)
pca_log2 = PCA()
pca_log2.fit(log2_x)
cum_var_log2 = np.cumsum(pca_log2.explained_variance_ratio_)

# Find number of PCs needed for 85% variance
n_components_raw = np.argmax(cum_var_raw >= 0.85) + 1
n_components_log2 = np.argmax(cum_var_log2 >= 0.85) + 1

print(f"Number of PCs needed for 85% variance (raw data): {n_components_raw}")
print(f"Number of PCs needed for 85% variance (log2 data): {n_components_log2}")

# Plot cumulative explained variance
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(cum_var_raw) + 1), cum_var_raw, 'b-', label='Raw data')
plt.plot(range(1, len(cum_var_log2) + 1), cum_var_log2, 'r-', label='Log2 data')
plt.axhline(y=0.85, color='g', linestyle='--', label='85% threshold')
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance Ratio')
plt.title('Explained Variance vs Number of Components')
plt.legend()
plt.grid(True)
plt.show()

# create a scatterplot using the first two coordinates
plt.figure(figsize=(10, 8))
plt.scatter(log2_x[:, 0], log2_x[:, 1], c=y, cmap='viridis', alpha=0.7)
plt.colorbar(label='Class')
plt.xlabel('First coordinate ([:, 0])')
plt.ylabel('Second coordinate (X[:, 1])')
plt.title('Scatterplot of First Two Coordinates')
plt.grid(True, alpha=0.3)
plt.show()



