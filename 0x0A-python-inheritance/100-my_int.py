#!/usr/bin/python3
"""Write a class MyInt that inherits from int"""


class MyInt(int):
    """Inverts int operators == and !=."""

    def __eq__(self, value):
        """Overides == with !=."""
        return self.real != value

    def __ne__(self, value):
        """Overide !=  with ==."""
        return self.real == value
