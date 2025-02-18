""" This is to be used for simple calculations related to homework problems"""
import numpy as np

def sample_covariance_matrix(vectors: list) -> np.ndarray:
    """
    Calculate sample covariance matrix for a list of column vectors.

    Args:
        vectors: List of column vectors (each as np.ndarray)

    Returns:
        np.ndarray: Sample covariance matrix S
    """
    # Number of samples
    n = len(vectors)

    # Calculate empirical mean
    X_bar = (1/n) * sum(vectors)

    # First term: (1/n)∑(X^(i)(X^(i))^T)
    first_term = (1/n) * sum(x @ x.T for x in vectors)

    # Second term: X_bar * X_bar^T
    second_term = X_bar @ X_bar.T

    # Sample covariance matrix S
    S = first_term - second_term

    return S

# Example usage:
x_1 = np.array([[8],[4],[7]])
x_2 = np.array([[2],[8],[1]])
x_3 = np.array([[3],[1],[1]])
x_4 = np.array([[9],[7],[4]])

vectors = [x_1, x_2, x_3, x_4]
S = sample_covariance_matrix(vectors)
print("Sample Covariance Matrix:")
print(S)

# Identity matrix (3x3)
I = np.eye(3)

# Vector of ones (3x1)
ones = np.ones((3, 1))

# Calculate H
n = 3
H = I - (1/n) * (ones @ ones.T)

print("H matrix:")
print(H)

## check if unit vector
u1 = 1/np.sqrt(5)
u2 = 2/np.sqrt(5)

magnitude = np.sqrt(u1**2 + u2**2)
print(magnitude)

# Define vectors
u = (1/np.sqrt(5)) * np.array([[1], [2]])  # u = (1/√5)(1,2)ᵀ
X1 = np.array([[1], [2]])                  # X₁ = (1,2)ᵀ
X2 = np.array([[3], [4]])                  # X₂ = (3,4)ᵀ
X3 = np.array([[-1], [0]])                 # X₃ = (-1,0)ᵀ

# Calculate signed distances (u·Xᵢ)
d1 = float(u.T @ X1)  # = (1/√5)(1×1 + 2×2) = (1/√5)(5) = √5 ≈ 2.236
d2 = float(u.T @ X2)  # = (1/√5)(1×3 + 2×4) = (1/√5)(11) = 11/√5 ≈ 4.919
d3 = float(u.T @ X3)  # = (1/√5)(1×(-1) + 2×0) = -1/√5 ≈ -0.447

distances = np.array([d1, d2, d3])

# Calculate empirical variance using numpy with ddof=1
variance = np.var(distances, ddof=1)

print(f"Signed distances:")
print(f"d1 = {d1}")
print(f"d2 = {d2}")
print(f"d3 = {d3}")
print(f"\nEmpirical variance = {variance}")

# Also calculate uᵀSu
X = np.array([[1, 2],    # X₁ᵀ
              [3, 4],    # X₂ᵀ
              [-1, 0]])  # X₃ᵀ

n = 3
I = np.eye(n)
ones = np.ones((n, 1))
H = I - (1/n) * (ones @ ones.T)
S = (1/n) * (X.T @ H @ X)
result = float(u.T @ S @ u)

print(f"uᵀSu = {result}")

import numpy as np
from stats.covariance import CovarianceMatrix

# Example 1: Using a list of column vectors
x1 = np.array([0.5,0.5])
x2 = np.array([0.5,2.5])


vectors = [x1, x2]
cov_matrix = CovarianceMatrix(vectors)
s = cov_matrix.compute()
print("Covariance matrix from vectors:")
print(S)

eig = CovarianceMatrix(vectors)
eigenvalues, eigenvectors = eig.eigendecomposition()
print("eigenvalues from vectors:")
print(eigenvectors)

x = np.array([[1, 1],
              [1, -1],
              [-1, 1]])

# Calculate Gram matrix B = XXᵀ
b = x @ x.T

print("Gram matrix B =")
print(b)

gram_matrix = np.array([[2, 0, 0],
              [0, 2, -2],
              [0, -2, 2]])

eigenvalues, eigenvectors = np.linalg.eigh(gram_matrix)

# Sort in descending order (λ₁ > λ₂ > λ₃)
idx = eigenvalues.argsort()[::-1]
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

print("Eigenvalues in descending order:")
print(f"λ₁ = {eigenvalues[0]}")
print(f"λ₂ = {eigenvalues[1]}")
print(f"λ₃ = {eigenvalues[2]}")

print("\nEigenvectors (as columns):")
print(eigenvectors)