import torch

from jaxtyping import Float


class PCA:
    """Perform Principal Component Analysis (PCA).

    Args:
        n_components (int): Number of components to keep.

    Attributes:
        components (Float[torch.Tensor, "n_components, n_features]):
        Principal axes in feature space, representing the directions of
        maxomum variance in the data.
    """

    def __init__(self, n_components: int):
        self.n_components = n_components

    def __call__(self, X: Float[torch.Tensor, "n_samples n_features"]):
        """Perform PCA on the given data.

        Args:
            X (Float[torch.Tensor, "n_samples n_features"]): The data on which PCA is performed.
        """
        raise NotImplementedError

    def fit(self, X: Float[torch.Tensor, "n_samples n_features"]):
        """Fit PCA on the given data.

        Args:
            X (Float[torch.Tensor, "n_samples n_features"]): The data on which PCA is to be fitted.
        """

        # 1. Find Covariance of X
        # 2. Find eigen values, and eigen vectors of X
        # 3. Sort the eigen vectors in decreasing order of explained variance
        # 4. Set self.components_
        # 5. Set self.components

        raise NotImplementedError
