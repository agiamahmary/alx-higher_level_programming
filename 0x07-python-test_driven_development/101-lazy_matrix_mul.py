#!/usr/bin/python3
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    arr_1 = np.array(m_a)
    arr_2 = np.array(m_b)
    return list(arr_1 * arr_2)
