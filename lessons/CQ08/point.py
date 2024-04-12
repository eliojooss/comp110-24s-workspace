"""OOP Practice."""

from __future__ import annotations

__author__ = "730484781"


class Point:
    """Point."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Create a new Point."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int):
        """Scale existing point."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point: 
        """Create a new Point scaled by a factor."""
        return Point(self.x * factor, self.y * factor)
