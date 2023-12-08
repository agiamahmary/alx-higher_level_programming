#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if type(m_a) == list:
        raise TypeError('m_a must be a list')
    if type(m_b) == list:
        raise TypeError('m_b must be a list')

    if m_a == [] or m_a == [[]]:
        raise ValueError('m_a can\'t be empty')
    if m_b == [] or m_b == [[]]:
        raise ValueError('m_b can\'t be empty')
    for row in m
