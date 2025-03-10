import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import os

# Load the data using the absolute path
x = np.load('/Users/nikos/Documents/GitHub/MITx_Statistics_and_Datascience/6.419x - Data Analysis Statistical Modeling and Computation in Applications/modules/module_2/data/p2_unsupervised/X.npy')

# Create log2 transformed data
x_log2 = np.log2(x + 1)

print("Shape of X:", x_log2.shape)

# Step 1: Project onto top 50 PCs
pca = PCA(n_components=50)
x_pca = pca.fit_transform(x_log2)

print(f"Variance explained by top 50 PCs: {sum(pca.explained_variance_ratio_):.4f}")

# Step 2: First identify the 3 main cell types
n_main_clusters = 3
kmeans_main = KMeans(n_clusters=n_main_clusters, random_state=42)
main_labels = kmeans_main.fit_predict(x_pca)

# Step 3: Now identify subtypes within each main type
# We'll use more clusters to find subtypes
n_subtypes = 9  # 3 subtypes per main type
kmeans_sub = KMeans(n_clusters=n_subtypes, random_state=42)
subtype_labels = kmeans_sub.fit_predict(x_pca)

# Step 4: Map each subtype to its main type
subtype_to_main = {}
for subtype in range(n_subtypes):
    # Find which main cluster this subtype mostly belongs to
    subtype_mask = subtype_labels == subtype
    if np.sum(subtype_mask) > 0:  # Ensure the subtype has points
        main_counts = np.bincount(main_labels[subtype_mask], minlength=n_main_clusters)
        main_type = np.argmax(main_counts)
        subtype_to_main[subtype] = main_type

# Step 5: Visualize with t-SNE - using max_iter instead of n_iter to fix the warning
tsne = TSNE(n_components=2,
            perplexity=30,
            early_exaggeration=12,
            learning_rate=200,
            max_iter=2000,  # Changed from n_iter to max_iter
            random_state=42)
x_tsne = tsne.fit_transform(x_pca)

# Create visualization
plt.figure(figsize=(14, 10))

# Main type colors
main_colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # Blue, Orange, Green
main_type_names = ['Excitatory Neurons', 'Inhibitory Neurons', 'Non-neuronal Cells']

# Plot each subtype with different markers but same main type color
markers = ['o', 's', '^']  # circle, square, triangle
for subtype in range(n_subtypes):
    if subtype in subtype_to_main:
        main_type = subtype_to_main[subtype]
        base_color = main_colors[main_type]

        # Use different marker for each subtype within the same main type
        marker_idx = subtype % 3

        subtype_mask = subtype_labels == subtype
        plt.scatter(x_tsne[subtype_mask, 0], x_tsne[subtype_mask, 1],
                   color=base_color,
                   marker=markers[marker_idx],
                   alpha=0.7,
                   s=50,
                   edgecolors='w',
                   linewidths=0.5)

# Add ellipses to highlight the main cell types
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms

def confidence_ellipse(x, y, ax, n_std=2.0, facecolor='none', **kwargs):
    """
    Create a plot of the covariance confidence ellipse of *x* and *y*.
    """
    if x.size != y.size:
        raise ValueError("x and y must be the same size")

    cov = np.cov(x, y)
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])

    # Using a special case to obtain the eigenvalues of this
    # two-dimensional dataset.
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0), width=ell_radius_x * 2, height=ell_radius_y * 2,
                      facecolor=facecolor, **kwargs)

    # Calculating the standard deviation of x from the square root of the variance
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)

    # Calculating the standard deviation of y from the square root of the variance
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)

    transf = transforms.Affine2D() \
        .rotate_deg(45) \
        .scale(scale_x, scale_y) \
        .translate(mean_x, mean_y)

    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)

# Add ellipses for each main type
ax = plt.gca()
for i in range(n_main_clusters):
    mask = main_labels == i
    confidence_ellipse(x_tsne[mask, 0], x_tsne[mask, 1], ax, n_std=2.0,
                      edgecolor=main_colors[i], linewidth=2,
                      label=f'Main Type: {main_type_names[i]}')

plt.xlabel('t-SNE Dimension 1', fontsize=14)
plt.ylabel('t-SNE Dimension 2', fontsize=14)
plt.title('Brain Cell Subtypes within Main Cell Types', fontsize=16)

# Create a custom legend for main types only
from matplotlib.lines import Line2D
legend_elements = []

# Add main types to legend
for i in range(n_main_clusters):
    legend_elements.append(Line2D([0], [0], color=main_colors[i], lw=2,
                                 label=f'{main_type_names[i]}'))

plt.legend(handles=legend_elements, loc='upper right', fontsize=12)
plt.grid(False)

plt.tight_layout()
plt.savefig('images/brain_cell_subtypes.png', dpi=300)
plt.show()