#!/usr/bin/python3
"""Contains a BaseGeometry class"""


class BaseGeometry:
    """A base class for geometry-related operations."""

    def area(self):
        """Raise an exception since area is not implemented."""
        raise Exception("area() is not implemented")
