#!/usr/bin/python3
"""Write a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """A Function that finds a peak in a list of unsorted integers.
    """
    if list_of_integers == []:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]

    pk_f = (len(list_of_integers) // 2)

    num = {'idx': 0, 'num': list_of_integers[0]}
    n_list = list_of_integers

    for idx in range(len(n_list)):
        if idx == len(n_list) - 1:
            if n_list[idx] >= n_list[idx - 1]:
                if (idx - num['idx'] - 1) <= pk_f:
                    num.update({'idx': idx})
                    num.update({'num': n_list[idx]})
        else:
            if n_list[idx] >= n_list[idx - 1] and \
            n_list[idx] >= n_list[idx + 1]:
                if (idx - num['idx'] - 1) <= pk_f:
                    num.update({'idx': idx})
                    num.update({'num': n_list[idx]})
    return num['num']
