import networkx as nx
import numpy as np

# Use the correct relative path
G = nx.read_edgelist('../directed_graph.txt', create_using=nx.DiGraph())

# Basic graph properties
print("Graph Properties:")
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")

# # Check if graph has cycles
# print("\nChecking for cycles...")
# try:
#     has_cycles = len(list(nx.simple_cycles(G))) > 0
#     print(f"Has cycles: {has_cycles}")
# except:
#     print("Cycle detection took too long - graph is too large")

# Get adjacency matrix (sparse format)
print("\nGetting adjacency matrix...")
adj_matrix = nx.adjacency_matrix(G)
print("Matrix shape:", adj_matrix.shape)

# Check for self-loops efficiently
print("\nChecking for self-loops...")
self_loops = list(nx.selfloop_edges(G))
print(f"Number of self-loops found: {len(self_loops)}")

# Basic degree analysis
print("\nDegree statistics:")
in_degrees = [d for n, d in G.in_degree()]
out_degrees = [d for n, d in G.out_degree()]
print(f"Max in-degree: {max(in_degrees)}")
print(f"Max out-degree: {max(out_degrees)}")
print(f"Average in/out-degree: {sum(in_degrees)/len(in_degrees):.2f}")

# Define adjacency matrix
A = np.array([
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 0]
])

# Define node types (1 for even indices, 2 for odd indices)
node_types = [1 if i % 2 == 0 else 2 for i in range(10)]

# Calculate total number of edges
m = np.sum(A) / 2  # Divide by 2 since undirected graph

# Initialize modularity
Q = 0

# Calculate modularity
for i in range(10):
    for j in range(10):
        if node_types[i] == node_types[j]:  # Same community
            ki = np.sum(A[i])  # Degree of node i
            kj = np.sum(A[j])  # Degree of node j
            Q += (A[i,j] - (ki * kj)/(2*m))

Q = Q/(2*m)

print(f"\nModularity Q = {Q:.4f}")