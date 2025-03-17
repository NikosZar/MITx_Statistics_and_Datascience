import numpy as np
import networkx as nx

# Create adjacency matrix
A = np.array([
    [0, 3, 0, 5, 2, 0],
    [3, 0, 5, 0, 2, 0],
    [0, 5, 0, 3, 0, 2],
    [5, 0, 3, 0, 0, 2],
    [2, 2, 0, 0, 0, 2],
    [0, 0, 2, 2, 2, 0]
])

# Create graph from adjacency matrix
G = nx.from_numpy_array(A)

# Compute shortest path distances between all pairs of nodes
D = nx.floyd_warshall_numpy(G)
print(D)


# Create kite graph with 8 nodes (numbered 1-8)
kite = nx.Graph()
kite.add_edges_from([
    (1, 2), (2, 3), (3, 4), (4, 1),  # Diamond shape
    (3, 5), (5, 6), (6, 7), (7, 8)   # Tail of kite
])

# Compute the Fiedler vector (eigenvector of second smallest eigenvalue)
fiedler = nx.fiedler_vector(kite)

print("\nFiedler vector for kite graph:")
for i, value in enumerate(fiedler, start=1):  # Start enumeration from 1 to match node numbering
    print(f"Node {i}: {value:.6f}")

