import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import os
from matplotlib.colors import LinearSegmentedColormap

# Load the data
x = np.load('/Users/nikos/Documents/GitHub/MITx_Statistics_and_Datascience/6.419x - Data Analysis Statistical Modeling and Computation in Applications/modules/module_2/data/p2_unsupervised/X.npy')

# Create log2 transformed data
x_log2 = np.log2(x + 1)

print("Shape of X:", x_log2.shape)

# Step 1: Project onto top 50 PCs to reduce dimensionality and noise
pca = PCA(n_components=50)
x_pca = pca.fit_transform(x_log2)

print(f"Variance explained by top 50 PCs: {sum(pca.explained_variance_ratio_):.4f}")

# Step 2: Run K-means with different numbers of clusters to find optimal k
max_clusters = 15
inertia_values = []

for k in range(1, max_clusters + 1):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(x_pca)
    inertia_values.append(kmeans.inertia_)
    print(f"K={k}, Inertia={kmeans.inertia_:.2f}")

# Step 3: Plot the elbow curve
plt.figure(figsize=(10, 6))
plt.plot(range(1, max_clusters + 1), inertia_values, 'bo-')
plt.xlabel('Number of Clusters (k)', fontsize=12)
plt.ylabel('Inertia (Within-Cluster Sum of Squares)', fontsize=12)
plt.title('Elbow Method for Optimal k', fontsize=14)
plt.grid(True, alpha=0.3)
plt.axvline(x=3, color='r', linestyle='--', label='k=3 (Main cell types)')
plt.axvline(x=9, color='g', linestyle='--', label='k=9 (Subtypes)')
plt.legend()
plt.tight_layout()
plt.savefig('images/kmeans_elbow_curve_revised.png', dpi=300)
plt.show()

# Step 4: First identify the 3 main cell types
k_main = 3
kmeans_main = KMeans(n_clusters=k_main, random_state=42, n_init=10)
main_labels = kmeans_main.fit_predict(x_pca)

# Step 5: For each main cluster, find subtypes
# We'll use hierarchical clustering within each main type
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch

# Number of subtypes to find within each main type
subtypes_per_main = 3
all_subtype_labels = np.zeros_like(main_labels)
next_label = 0

# Run t-SNE for visualization
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, random_state=42)
x_tsne = tsne.fit_transform(x_pca)

# Create distinct color palettes for each main type
# Blue palette for type 1
blues = ['#c6dbef', '#6baed6', '#2171b5']
# Orange palette for type 2
oranges = ['#fdd0a2', '#fd8d3c', '#d94701']
# Green palette for type 3
greens = ['#c7e9c0', '#74c476', '#238b45']

# Combined color palette for all subtypes
all_colors = blues + oranges + greens

# Process each main cluster
for i in range(k_main):
    # Get data points belonging to this main cluster
    mask = main_labels == i
    x_main = x_pca[mask]

    if len(x_main) > subtypes_per_main:  # Ensure we have enough points
        # Apply hierarchical clustering to find subtypes
        # Plot dendrogram to visualize hierarchical structure
        plt.figure(figsize=(10, 6))
        dendrogram = sch.dendrogram(sch.linkage(x_main, method='ward'))
        plt.title(f'Dendrogram for Main Cell Type {i+1}', fontsize=14)
        plt.xlabel('Data Points', fontsize=12)
        plt.ylabel('Euclidean Distance', fontsize=12)
        plt.savefig(f'images/dendrogram_main_type_{i+1}.png', dpi=300)
        plt.close()

        # Apply Agglomerative Clustering
        agg_clustering = AgglomerativeClustering(n_clusters=subtypes_per_main, linkage='ward')
        subtype_labels = agg_clustering.fit_predict(x_main)

        # Assign global labels
        for j in range(subtypes_per_main):
            submask = np.zeros_like(main_labels, dtype=bool)
            submask[mask] = (subtype_labels == j)
            all_subtype_labels[submask] = next_label
            next_label += 1
    else:
        # If too few points, keep as one cluster
        all_subtype_labels[mask] = next_label
        next_label += 1

# Create the final visualization with improved colors
plt.figure(figsize=(14, 10))

# Plot each subtype with its own color
for i in range(next_label):
    mask = all_subtype_labels == i
    plt.scatter(x_tsne[mask, 0], x_tsne[mask, 1],
               color=all_colors[i],
               s=60, alpha=0.8,
               edgecolors='w', linewidths=0.5,
               label=f'Subtype {i+1}')

# Add a legend with a reasonable size
plt.xlabel('t-SNE Dimension 1', fontsize=14)
plt.ylabel('t-SNE Dimension 2', fontsize=14)
plt.title('Cell Types and Subtypes', fontsize=16)

# Create a more compact legend
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
plt.grid(False)
plt.tight_layout()
plt.savefig('images/cell_types_and_subtypes_improved.png', dpi=300)
plt.show()

# Create a second visualization that shows main types more clearly
plt.figure(figsize=(14, 10))

# Main type colors
main_colors = ['#3182bd', '#e6550d', '#31a354']  # Darker blue, orange, green
main_type_names = ['Excitatory Neurons', 'Inhibitory Neurons', 'Non-neuronal Cells']

# Plot each main type with a distinct color
for i in range(k_main):
    mask = main_labels == i
    plt.scatter(x_tsne[mask, 0], x_tsne[mask, 1],
               color=main_colors[i],
               s=60, alpha=0.7,
               label=f'{main_type_names[i]}')

plt.xlabel('t-SNE Dimension 1', fontsize=14)
plt.ylabel('t-SNE Dimension 2', fontsize=14)
plt.title('Three Main Cell Types', fontsize=16)
plt.legend(fontsize=12)
plt.grid(False)
plt.tight_layout()
plt.savefig('images/main_cell_types.png', dpi=300)
plt.show()

# Save the final subtype labels
np.save('images/subtype_labels.npy', all_subtype_labels)

# Count the number of cells in each subtype
unique_subtypes = np.unique(all_subtype_labels)
print(f"\nTotal number of subtypes identified: {len(unique_subtypes)}")
for i in unique_subtypes:
    print(f"Subtype {i+1}: {np.sum(all_subtype_labels == i)} cells")