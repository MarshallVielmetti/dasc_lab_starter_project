import numpy as np

from .dynamics_model import DynamicsModel


class KinematicBicycle2D(DynamicsModel):
    """Class representing a system with Kinematic 2D Bicycle."""

    def __init__(self, L: np.float32):
        """
        L: Bicycle Length
        """
        self.L = L

    def f(self, x: np.ndarray, u: np.ndarray) -> np.ndarray:
        """
        X: [x, y, theta, delta]^T -- theta is heading angle, delta is steering angle
        U: [v, phi]^T -- velocity and steering rate
        """
        raise NotImplementedError("Exercise kinematic-bicycle-2d is not implemented")
