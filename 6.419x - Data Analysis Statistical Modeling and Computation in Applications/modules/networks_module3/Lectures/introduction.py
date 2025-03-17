import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Graph 1
G1 = nx.DiGraph()  # Directed graph since it's marked as directed in the image
vertices1 = [1, 2, 3, 4, 5]
edges1 = [(1,2), (2,3), (3,4), (4,5), (5,2)]

G1.add_nodes_from(vertices1)
G1.add_edges_from(edges1)

# Test properties for Graph 1
print("Graph 1 Properties:")
print(f"Is directed: {nx.is_directed(G1)}")
has_cycle = len(list(nx.simple_cycles(G1))) > 0
print(f"Has cycles: {has_cycle}")
print(f"Is acyclic: {nx.is_directed_acyclic_graph(G1)}")

# Graph 2
G2 = nx.DiGraph()  # Directed graph
vertices2 = [1, 2, 3, 4, 5]
edges2 = [(1,2), (1,4), (3,4), (4,5), (5,2)]

G2.add_nodes_from(vertices2)
G2.add_edges_from(edges2)

print("\nGraph 2 Properties:")
print(f"Is directed: {nx.is_directed(G2)}")
has_cycle2 = len(list(nx.simple_cycles(G2))) > 0
print(f"Has cycles: {has_cycle2}")
print(f"Is acyclic: {nx.is_directed_acyclic_graph(G2)}")

# Visualize both graphs
plt.figure(figsize=(12, 5))

plt.subplot(121)
nx.draw(G1, with_labels=True, node_color='lightblue',
        node_size=500, arrowsize=20)
plt.title("Graph 1")

plt.subplot(122)
nx.draw(G2, with_labels=True, node_color='lightblue',
        node_size=500, arrowsize=20)
plt.title("Graph 2")

plt.show()



# Create a multigraph (since it's marked as multigraph in the image)
G = nx.MultiGraph()  # Undirected multigraph

# Add vertices and edges
vertices = [1, 2, 3, 4, 5]
edges = [(1,2), (1,4), (3,1), (4,5), (5,2)]

G.add_nodes_from(vertices)
G.add_edges_from(edges)

# Test properties
print("Graph Properties:")
print(f"Is multigraph: {isinstance(G, nx.MultiGraph)}")
print(f"Is bipartite: {nx.is_bipartite(G)}")
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")

# Visualize the graph
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue',
        node_size=500, width=2)
plt.title("Multigraph")
plt.show()

# Adjacency matrix


# Create adjacency matrix and visualize walks
matrix = np.array([
    [1, 1, 0],
    [0, 0, 1],
    [1, 0, 0]
])

g_adj = nx.from_numpy_array(matrix)
adj_matrix = nx.adjacency_matrix(g_adj).todense()

# Visualize the graph
plt.figure(figsize=(8, 6))
nx.draw(g_adj, with_labels=True, node_color='lightblue',
        node_size=500, width=2)
plt.title("Graph from Adjacency Matrix")

# Display adjacency matrix
print("\nAdjacency Matrix:")
print(adj_matrix)

# Calculate and display walks of different lengths
print("\nNumber of walks of length:")
for k in range(1, 4):
    walks = np.linalg.matrix_power(adj_matrix, k)
    print(f"{k}: \n{walks}")

# Define the adjacency matrix
A = np.array(	[[0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
	[1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
	[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
	[1, 1, 0, 0, 0, 1, 0, 1, 1, 0],
	[0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
	[1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
	[0, 0, 0, 0, 1, 0, 1, 0, 1, 0]])

# Calculate A^2 for walks of length 2
A2 = np.linalg.matrix_power(A, 2)
print("A^2 (walks of length 2):")
print(A2)
print(f"Number of walks of length 2 from node 1 to 2: {A2[0,1]}")

# Calculate A^3 for walks of length 3
A3 = np.linalg.matrix_power(A, 3)
print("\nA^3 (walks of length 3):")
print(A3)
print(f"Number of walks of length 3 from node 1 to 2: {A3[0,1]}")

# Calculate A^5
A5 = np.linalg.matrix_power(A, 5)

# Get number of walks from node 0 to itself
walks_0_to_0 = A5[0,0]

print(f"Number of walks of length 5 from node 0 to itself: {int(walks_0_to_0)}")

# Check if it's a simple graph
print("Checking if this is a simple graph:")

# 1. Check for self-loops (diagonal elements should be 0)
has_self_loops = np.any(np.diag(A) != 0)
print(f"Has self-loops: {has_self_loops}")

# 2. Check for multiple edges (all elements should be 0 or 1)
has_multiple_edges = np.any((A != 0) & (A != 1))
print(f"Has multiple edges: {has_multiple_edges}")

# 3. Check if undirected (matrix should be symmetric)
is_symmetric = np.array_equal(A, A.T)
print(f"Is symmetric: {is_symmetric}")

# Conclusion
is_simple = not has_self_loops and not has_multiple_edges and is_symmetric
print(f"\nThis is{' ' if is_simple else ' not '}a simple graph")

# Function to check if matrix has any zeros
def has_zeros(matrix):
    return np.any(matrix == 0)

# Test increasing powers until we find one with no zeros
lambda_value = 1
while lambda_value <= 20:  # Set a reasonable upper limit
    power_matrix = np.linalg.matrix_power(A, lambda_value)
    if not has_zeros(power_matrix):
        print(f"Found! Minimum lambda = {lambda_value}")
        print(f"\nA^{lambda_value}:")
        print(power_matrix)
        break
    lambda_value += 1

    if lambda_value % 5 == 0:  # Print progress every 5 steps
        print(f"Checked up to lambda = {lambda_value}")

# Create graph from adjacency matrix
G = nx.from_numpy_array(A)

# Find connected components
components = list(nx.connected_components(G))

# Print results
print(f"Number of connected components: {len(components)}")
print("\nComponents:")
for i, component in enumerate(components, 1):
    print(f"Component {i}: {sorted(list(component))}")

# Visualize components with different colors
plt.figure(figsize=(10, 8))
colors = ['lightblue', 'lightgreen', 'lightpink', 'lightyellow']
pos = nx.spring_layout(G)
for i, comp in enumerate(components):
    nx.draw_networkx_nodes(G, pos, nodelist=list(comp),
                          node_color=colors[i % len(colors)],
                          node_size=500)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
plt.title("Graph with Connected Components")
plt.show()