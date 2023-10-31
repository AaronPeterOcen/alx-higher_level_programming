#!/usr/bin/python3
def matrix_divided(matrix, div):
    try:
        if div == 0:
            raise ZeroDivisionError("")

        if not isinstance(div, (int, float)):
            raise TypeError("")

        leng = len(matrix[0])
        if not all(len(y) == leng for y in matrix):
            raise TypeError("")

        for one in matrix:
            if not all(isinstance(x, (int, float)) for x in one):
                raise TypeError("")
    except TypeError as e:
        print("TypeError: {}".format(e))
        return None
    except ZeroDivisionError as e:
        print("ZeroDivisionError: {}".format(e))
        return None

    new_matrix = []
    for one in matrix:
        new_matrix.append([round(x / div, 2) for x in one])
    return new_matrix
