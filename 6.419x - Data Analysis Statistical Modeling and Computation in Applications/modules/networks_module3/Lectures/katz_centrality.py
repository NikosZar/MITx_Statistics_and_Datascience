import networkx as nx
import numpy as np

A = np.array([[0, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0]])

# Create graph and use NetworkX's implementation
G = nx.from_numpy_array(A, create_using=nx.DiGraph())
centrality = nx.katz_centrality(G, alpha=0.1, beta=1)

print("\nKatz centrality:")
for node, score in centrality.items():
    print(f"Node {node}: {score:.4f}")

page_rank = nx.pagerank(G, alpha=0.85)

print("\nPagerank centrality:")
for node, score in page_rank.items():
    print(f"Node {node}: {score:.4f}")

# Calculate HITS hub and authority scores
hits = nx.hits(G)
hub_scores = hits[0]  # First element contains hub scores
authority_scores = hits[1]  # Second element contains authority scores

print("\nHITS Hub scores:")
for node, score in hub_scores.items():
    print(f"Node {node}: {score:.4f}")

print("\nHITS Authority scores:")
for node, score in authority_scores.items():
    print(f"Node {node}: {score:.4f}")