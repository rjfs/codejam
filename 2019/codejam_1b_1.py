# Alien Rhyme
import time
import numpy as np


def get_coordinate(m, M, P, Q):
    m_order = sorted(m.keys())
    M_order = sorted(M.keys())
    n_m = 0  # relative to origin
    n_M = 0  # relative to origin
    x = 0
    n_x = 0

    for i, pm in enumerate(M_order):
        x_cand = pm + 1
        n_M += M[pm]

        while len(m_order) > 0 and m_order[0] <= x_cand:
            n_m -= m[m_order.pop(0)]

        if n_m + n_M > n_x:
            n_x = n_m + n_M
            x = x_cand
        else:
            break

    return max(min(x, Q), 0)


def find_solution_old(P, Q, people):
    yM = {}
    ym = {}
    xM = {}
    xm = {}
    for x, y, d in people:
        if d == 'W':
            try:
                xm[x] += 1
            except KeyError:
                xm[x] = 1
        elif d == 'E':
            try:
                xM[x] += 1
            except KeyError:
                xM[x] = 1
        elif d == 'N':
            try:
                yM[y] += 1
            except KeyError:
                yM[y] = 1
        else:
            try:
                ym[y] += 1
            except KeyError:
                ym[y] = 1

    return get_coordinate(xm, xM, P, Q), get_coordinate(ym, yM, P, Q)


def get_test_cross(center):
    x, y = center
    assert x > 0 and y > 0
    return tuple([
        (x - 1, y, 'E'),
        (x + 1, y, 'W'),
        (x, y + 1, 'S'),
        (x, y - 1, 'N'),
    ])


def find_solution(P, Q, people):
    table = np.zeros((Q + 1, Q + 1))
    for x, y, d in people:
        if d == 'W':
            table[:x, :] += 1
        elif d == 'E':
            table[x + 1:, :] += 1
        elif d == 'N':
            table[:, y + 1:] += 1
        else:
            table[:, :y] += 1
    print(table)
    mx = np.argmax(table)
    return mx // Q, mx % Q


def run_tests():
    tests = [
        #(((4, 10), ((0, 9, 'N'), (1, 10, 'W'), (9, 0, 'E'), (10, 1, 'S'))), (0, 0)),
        #(((1, 10), ((5, 5, 'N'),)), (0, 6)),
        (((4, 10), ((2, 4, 'N'), (2, 6, 'S'), (1, 5, 'E'), (3, 5, 'W'))),
         (2, 5)),
        (((8, 10), (
        (0, 2, 'S'), (0, 3, 'N'), (0, 3, 'N'), (0, 4, 'N'), (0, 5, 'S'),
        (0, 5, 'S'), (0, 8, 'S'), (1, 5, 'W'))), (0, 4)),
        (((3, 10), ((0, 0, 'E'), (1, 0, 'E'), (2, 0, 'E'))), (3, 0)),
        (((3, 10), ((2, 0, 'N'), (0, 1, 'E'), (2, 2, 'S'))), (1, 1)),
        (((3, 10), ((1, 1, 'N'), (1, 1, 'E'), (1, 1, 'S'))), (2, 0)),
        (((4, 10), ((1, 1, 'N'), (1, 1, 'E'), (1, 1, 'S'), (1, 1, 'W'))),
         (0, 0)),
        (((4, 10), get_test_cross((1, 1))), (1, 1)),
        (((4, 10), get_test_cross((3, 8)) + get_test_cross((8, 3))), (3, 3)),

    ]
    for i_t, (((P, Q), people), expected_res) in enumerate(tests):
        t0 = time.time()
        res = find_solution(P, Q, people)
        t = time.time() - t0
        print(res)
        assert res[0] == expected_res[0]
        assert res[1] == expected_res[1]
        print('Test %d ran in %.2f seconds' % (i_t + 1, t))


def std_in_out():
    t = int(input())  # read number of tests
    for t_i in range(1, t + 1):
        P, Q = tuple(int(i) for i in input().split())
        people = []
        for _ in range(P):
            l = input().split()
            people.append((int(l[0]), int(l[1]), l[2]))

        res = find_solution(P, Q, people)
        print("Case #{}: {} {}".format(t_i, res[0], res[1]))


run_tests()