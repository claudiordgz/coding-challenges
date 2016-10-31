"""
You are given a 2D matrix, a, of dimension MxN and a positive integer R.
You have to rotate the matrix R times and print the resultant matrix.
Rotation should be in anti-clockwise direction.
It is guaranteed that the minimum of M and N will be even.

Input Format
First line contains three space separated integers, M, N and R, where M is the number of rows,
N is number of columns in matrix, and R is the number of times the matrix has to be rotated.
Then M lines follow, where each line contains N space separated positive integers.
These M lines represent the matrix.

Constraints
2 <= M, N <= 300
1 <= R <= 10^9
min(M, N) % 2 == 0
1 <= a_ij <= 10^8, where i ∈ [1..M] & j ∈ [1..N]

Output Format
Print the rotated matrix.

"""
from fixture import get_testcase, read_raw
import itertools


def shift(seq, n):
    n %= len(seq)
    return seq[n:] + seq[:n]


def matrix_layer_rotation(matrix, rows, columns, rotations):
    """ Rotate a matrix to the left cell by cell

    :param matrix: [[],[],[]]
    :param rows:
    :param columns:
    :param rotations: the number or cells the matrix must be
        rotated
    :return: a rotated matrix
    """

    def iterate_layer(begin_rows, end_rows, begin_columns, end_columns):
        def _f(first_row, last_column, last_row, first_column):
            # first row
            for j in range(begin_columns, end_columns):
                first_row(j)

            # last column
            for i in range(begin_rows + 1, end_rows):
                last_column(i)

            # last row
            for j in reversed(range(begin_columns, end_columns - 1)):
                last_row(j)

            # first column
            for i in reversed(range(begin_rows + 1, end_rows - 1)):
                first_column(i)
        return _f

    def get_array(it, begin_rows, end_rows, begin_columns, end_columns):
        a = []
        it(lambda index: a.append(matrix[begin_rows][index]),
           lambda index: a.append(matrix[index][end_columns - 1]),
           lambda index: a.append(matrix[end_rows - 1][index]),
           lambda index: a.append(matrix[index][begin_columns]))
        return a

    def modify_matrix(it, arr, begin_rows, end_rows, begin_columns, end_columns):
        counter = itertools.count(0, 1)

        def first_row(index): matrix[begin_rows][index] = arr[next(counter)]

        def last_column(index): matrix[index][end_columns - 1] = arr[next(counter)]

        def last_row(index): matrix[end_rows - 1][index] = arr[next(counter)]

        def first_column(index): matrix[index][begin_columns] = arr[next(counter)]
        it(first_row,
           last_column,
           last_row,
           first_column)

    # how many arrays we need, min is guaranteed to be even
    n_layers = min(rows, columns) // 2

    # assemble my arrays from the matrix
    for k in range(n_layers):
        m_first = k    # first row
        n_first = k    # first column
        m_last = rows - k     # last row
        n_last = columns - k     # last column
        # retrieve arrays to rotate from matrix
        curried_iteration = iterate_layer(m_first, m_last, n_first, n_last)
        layer = get_array(curried_iteration, m_first, m_last, n_first, n_last)
        # rotate the thing
        layer = shift(layer, rotations)
        # insert into matrix
        modify_matrix(curried_iteration, layer, m_first, m_last, n_first, n_last)

    return matrix


def main():
    for t in ['02', '00', '01']:
        i, o = get_testcase(t, read_as=read_raw, folder_name='testcases/matrix_layer_rotation')
        data = list(map(int, i[0].split()))
        l = i[1:]
        l = [list(map(int, e.split())) for e in l]
        print(matrix_layer_rotation(l, data[0], data[1], data[2]))

if __name__ == '__main__':
    main()
