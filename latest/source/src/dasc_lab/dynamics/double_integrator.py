import numpy as np

from .linear import LinearDynamics


class DoubleIntegrator(LinearDynamics):
    """Class representing a generic double integrator."""

    def __init__(self, n: int):
        """Define the system matrices for an n-dimensional double integrator, and pass them to the constructor for the LinearSystem superclass."""
        raise NotImplementedError("Exercise double-integrator is not implemented")
