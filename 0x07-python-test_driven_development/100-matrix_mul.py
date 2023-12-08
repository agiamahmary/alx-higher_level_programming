#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError('m_a can\'t be empty')
    if m_b == [] or m_b == [[]]:
        raise ValueError('m_b can\'t be empty')

    row_a = len(m_a[0])
    row_b = len(m_b[0])

    for row in m_a:
        if len(row) != row_a:
            raise TypeError("each row of m_a must be of the same size")
        for col in row:
            if not isinstance(col, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if len(row) != row_b:
            raise TypeError("each row of m_b must be of the same size")
        for col in row:
            if not isinstance(col, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    new_matrix = []
    row_no = 0
    for row in m_a:
        col_fil = []
        for j in range(len(m_b[0])):
            col_val = 0
            for i in range(len(row)):
                col_val += row[i] * m_b[i][j]
            col_fil.append(col_val)
        new_matrix.append(col_fil)
    return new_matrix
