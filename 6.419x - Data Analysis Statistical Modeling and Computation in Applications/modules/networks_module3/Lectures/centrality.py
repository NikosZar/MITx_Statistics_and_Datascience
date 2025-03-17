import networkx as nx
import numpy as np

A = np.array([[1,1,1,1],
              [1,0,0,0],
              [1,0,0,0],
              [1,0,0,0]])

# Create graph and use NetworkX's implementation
G = nx.from_numpy_array(A, create_using=nx.DiGraph())
centrality = nx.eigenvector_centrality(G)

print("\nEigenvector centrality:")
for node, score in centrality.items():
    print(f"Node {node}: {score:.4f}")