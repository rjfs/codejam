def find_solution(n, matrix):
    trace = 0
    n_rows = 0
    n_cols = 0
    cols = [set() for _ in range(n)]
    for i in range(n):
        row = matrix[i]
        trace += row[i]
        row_set = set()
        for j, c in enumerate(row):
            cols[j].add(c)
            row_set.add(c)

        if len(row_set) != n:
            n_rows += 1

    for sc in cols:
        if len(sc) != n:
            n_cols += 1

    return "%s %s %s" % (trace, n_rows, n_cols)


def std_in_out():
    t = int(input())  # read number of tests
    for t_i in range(1, t + 1):
        N = int(input())
        lists = [tuple(int(i) for i in input().split()) for _ in range(N)]
        res = find_solution(N, lists)
        print("Case #{}: {}".format(t_i, res))


if __name__ == "__main__":
    std_in_out()
