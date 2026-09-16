import numpy as np

from .dynamics_model import DynamicsModel


class PlanarQuadrotor(DynamicsModel):
    """Class representing a 2D planar quadrotor."""

    g = 9.81

    def __init__(self, L: np.float32, M: np.float32, I: np.float32):
        self.L = L
        self.M = M
        self.I = I

    def f(self, x: np.ndarray, u: np.ndarray) -> np.ndarray:
        """
        X: [x, z, theta, x_dot, z_dot, theta_dot]^T
        U: [F_a, F_b]^T
        """
        raise NotImplementedError("Exercise planar-quadrotor is not implemented")
