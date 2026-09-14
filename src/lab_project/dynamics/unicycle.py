"""Small completed implementation used only for contract validation."""


class UnicycleDynamics:
    """Return a simple forward-motion derivative."""

    def f(self, state: tuple[float, float], speed: float) -> tuple[float, float]:
        raise NotImplementedError("Exercise unicycle-dynamics is not implemented")
