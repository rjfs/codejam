# Cherry mesh
import time


def get_groups(groups, conn):
    a, b = conn
    out = (-1, -1)
    for i, g in enumerate(groups):
        if a in g:
            out = (i, out[1])
        if b in g:
            out = (out[0], i)

    return min(out), max(out)  # ordered indexes


def find_solution(N, M, connections):
    sugar = 0
    n_groups = N
    groups = [{g} for g in range(1, N + 1)]
    for c in connections:
        i, j = get_groups(groups, c)
        if i != j:
            g1 = groups.pop(j)
            g2 = groups.pop(i)
            groups.append(g1 | g2)
            sugar += 1
            n_groups -= 1

    # return sugar + added red connections
    return sugar + 2*(n_groups - 1)


def run_tests():
    tests = [
        (2, [(1, 2)], 1),
        (3, [(2, 3)], 3),
        (3, [(1, 2), (2, 3), (1, 3)], 2),
        (4, [(1, 2), (2, 3), (1, 3)], 4),
        (4, [], 6),
        (1, [], 0),
        (4, [(2, 3), (1, 2), (1, 3)], 4),
        (4, [(1, 2), (3, 4), (2, 3), (1, 3)], 3),
    ]
    for i_t, (N, connections, expected_res) in enumerate(tests):
        M = len(connections)
        assert M <= N * (N-1) / 2
        t0 = time.time()
        res = find_solution(N, M, connections)
        t = time.time() - t0
        print("Case #{}: {}".format(i_t + 1, res))
        print('Test %d ran in %.2f seconds' % (i_t + 1, t))
        assert res == expected_res


def std_in_out():
    t = int(input())  # read number of tests
    for t_i in range(1, t + 1):
        N, M = (int(i) for i in input().split())
        connections = [tuple(int(i) for i in input().split()) for _ in range(M)]
        res = find_solution(N, M, connections)
        print("Case #{}: {}".format(t_i, res))


if __name__ == "__main__":
    std_in_out()
