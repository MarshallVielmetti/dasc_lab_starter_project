import numpy as np

from .dynamics_model import DynamicsModel


class DynamicUnicycle2D(DynamicsModel):
    """Class representing a system with Dynamic 2D Unicycle Dynamics."""

    def f(self, x: np.ndarray, u: np.ndarray) -> np.ndarray:
        """
        X: [x, y, theta, v]^T
        U: [a, omega]^T
        """
        raise NotImplementedError("Exercise dynamic-unicycle-2d is not implemented")
