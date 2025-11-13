import numpy as np


def svd(A, full_matrices: bool = False):
    """Compute SVD of matrix A and return (U, s, VT)."""
    U, s, VT = np.linalg.svd(A, full_matrices=full_matrices)
    return U, s, VT


def reconstruct(U, s, VT):
    """Reconstruct matrix from SVD components (U, s, VT)."""
    return U @ np.diag(s) @ VT


if __name__ == "__main__":
    A = np.array([[3, 1, 1],
                  [-1, 3, 1]], dtype=float)
    U, s, VT = svd(A, full_matrices=False)
    A_rec = reconstruct(U, s, VT)
    print("A:\n", A)
    print("U shape:", U.shape, " s shape:", s.shape, " VT shape:", VT.shape)
    print("Reconstrucción (A_rec) ≈ A:\n", A_rec)
