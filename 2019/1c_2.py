# Alien Rhyme
import time
import numpy as np


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
        (((3, 10), ((0, 0, 'E'), (1, 0, 'E'), (2, 0, 'E'))), (3, 0)),
        (((3, 10), ((2, 0, 'N'), (0, 1, 'E'), (2, 2, 'S'))), (1, 1)),
        (((3, 10), ((1, 1, 'N'), (1, 1, 'E'), (1, 1, 'S'))), (2, 0)),

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
