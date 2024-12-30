import torch
from jaxtyping import Float


class PCA:
    """Perform Principal Component Analysis (PCA).

    Args:
        n_components (int): Number of components to keep.

    Attributes:
        components (Float[torch.Tensor, "n_components n_features"]):
            Principal axes in feature space, representing the directions of
            maximum variance in the data.
        explained_variance (Float[torch.Tensor, "n_components"]):
            Variance explained by each of the selected components.
    """

    def __init__(self, n_components: int):
        self.n_components = n_components
        self.components = None
        self.explained_variance = None

    def fit(self, X: Float[torch.Tensor, "n_samples n_features"]):
        """Fit PCA on the given data.

        Args:
            X (Float[torch.Tensor, "n_samples n_features"]): The data on which PCA is to be fitted.
        """
        # 1. Center the data
        X_mean = X.mean(dim=0)
        X_centered = X - X_mean

        # 2. Compute the covariance matrix
        covariance_matrix = torch.mm(X_centered.T, X_centered) / (X.shape[0] - 1)

        # 3. Compute eigenvalues and eigenvectors
        eigenvalues, eigenvectors = torch.linalg.eigh(covariance_matrix)

        # 4. Sort eigenvectors by eigenvalues in descending order
        sorted_indices = torch.argsort(eigenvalues, descending=True)
        eigenvalues = eigenvalues[sorted_indices]
        eigenvectors = eigenvectors[:, sorted_indices]

        # 5. Select the top `n_components` eigenvectors
        self.components = eigenvectors[:, :self.n_components]
        self.explained_variance = eigenvalues[:self.n_components]

    def transform(self, X: Float[torch.Tensor, "n_samples n_features"]):
        """Apply the dimensionality reduction to the data.

        Args:
            X (Float[torch.Tensor, "n_samples n_features"]): The data to transform.

        Returns:
            Float[torch.Tensor, "n_samples n_components"]: The transformed data.
        """
        if self.components is None:
            raise RuntimeError("PCA not fitted. Call 'fit' first.")

        # Center the data
        X_mean = X.mean(dim=0)
        X_centered = X - X_mean

        # Project data onto principal components
        return torch.mm(X_centered, self.components)

    def fit_transform(self, X: Float[torch.Tensor, "n_samples n_features"]):
        """Fit PCA on the data and transform it.

        Args:
            X (Float[torch.Tensor, "n_samples n_features"]): The data to fit and transform.

        Returns:
            Float[torch.Tensor, "n_samples n_components"]: The transformed data.
        """
        self.fit(X)
        return self.transform(X)
