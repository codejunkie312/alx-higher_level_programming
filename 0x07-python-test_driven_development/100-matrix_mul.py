#!/usr/bin/python3
"""A module that includes a function that multiplies two matrices."""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        A new matrix that is the product of m_a and m_b.

    Raises:
        TypeError: If m_a or m_b are not lists.
        TypeError: If m_a or m_b are not lists of lists.
        ValueError: If m_a or m_b are empty lists/matrices.
        TypeError: If m_a or m_b contain a non int/float.
        TypeError: If m_a or m_b are not rectangular.
    """
    for mat, name in [(m_a, 'm_a'), (m_b, 'm_b')]:
        if not isinstance(mat, list):
            raise TypeError(f"{name} must be a list")
        if not all(isinstance(row, list) for row in mat):
            raise TypeError(f"{name} must be a list of lists")
        if len(mat) == 0 or len(mat[0]) == 0:
            raise ValueError(f"{name} can't be empty")
        row_length = len(mat[0])
        for row in mat:
            if len(row) != row_length:
                raise TypeError(f"each row of {name} must be of the same size")
            if not all(isinstance(x, (int, float)) for x in row):
                raise TypeError(f"{name} should contain only\
 integers or floats")

    rows_m_a, cols_m_a = len(m_a), len(m_a[0])
    rows_m_b, cols_m_b = len(m_b), len(m_b[0])

    if cols_m_a != rows_m_b:
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(rows_m_a):
        result_row = []
        for j in range(cols_m_b):
            value = 0
            for k in range(cols_m_a):
                value += m_a[i][k] * m_b[k][j]
            result_row.append(value)
        result.append(result_row)

    return result
