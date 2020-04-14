def solve(s):
    if s == 1:
        return [(1, 1)]
    path = [(1, 1), (2, 1)]
    path_sum = 2
    tri = [[1], [1, 1]]
    i, j = 1, 0
    while path_sum < s:
        if i == len(tri) - 1:
            tri.append(next_row(tri[-1]))

        a = tri[i+1][j]
        b = tri[i+1][j+1]
        c = tri[i][j+1] if j < len(tri[i]) - 1 else None

        if (b >= a and path_sum + sum(tri[i+1][j+1:]) <= s) or (path_sum + b == s) or (c is None):
            i += 1
            j += 1
        elif (path_sum + a == s) or (a > b and path_sum + sum(tri[i+1][j:]) <= s):
            i += 1
        elif path_sum + sum(tri[i + 1][j + 1:]) <= s:
            i += 1
            j += 1
        else:
            j += 1

        path.append((i + 1, j + 1))
        path_sum += tri[i][j]

    assert path_sum == s, "%s [%s!=%s]" % (path, path_sum, s)
    assert len(path) <= 500
    assert len(path) == len(set(path))

    return path


def next_row(row):
    return [l + r for l, r in zip(row + [0], [0] + row)]


if __name__ == "__main__":
    t = int(input())  # read number of tests
    for t_i in range(1, t + 1):
        res = solve(int(input()))
        print("Case #{}:".format(t_i))
        for pos in res:
            print("%s %s" % pos)
