"""This module provides utility functions for OpenDart API."""


def str_to_int(v: str) -> int:
    """Converts a string to an integer.

    Args:
        v (str): The string to be converted.

    Returns:
        int: The integer value of the string. If the string is "-", returns 0.
    """
    if not v or v == "-":
        return 0
    return int(v.replace(",", ""))


def str_to_float(v: str) -> float:
    """Converts a string to a float value.

    Args:
        v (str): The string to be converted.

    Returns:
        float: The float value of the input string.
    """
    if not v or v == "-":
        return 0.0

    return float(v.replace(",", ""))
