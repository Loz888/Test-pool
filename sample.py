"""A synthetic target for repository experiments; no network or file access."""

from collections.abc import Iterable


def total_points(points: Iterable[int]) -> int:
    """Total integer game points, rejecting booleans and non-integer values."""
    total = 0
    for point in points:
        if type(point) is not int:
            raise TypeError("points must contain only integers")
        total += point
    return total
