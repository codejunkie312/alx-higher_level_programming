#!/usr/bin/python3
"""A module that includes a function that multiplies two matrices."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        A new matrix that is the product of
        m_a and m_b.
    """
    return np.matmul(m_a, m_b)
