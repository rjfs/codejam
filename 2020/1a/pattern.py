def solve(patterns, n):
    starts = set()
    middles = set()
    ends = set()
    for p in patterns:
        start, *mids, end = p.split("*")
        starts.add(start)
        middles.add("".join(mids))
        ends.add(end)
    s = ""
    while starts:
        s2 = starts.pop()
        if len(s2) >= len(s):
            if not s2.startswith(s):
                return "*"
            s = s2
        else:
            if not s.startswith(s2):
                return "*"
    e = ""
    while ends:
        e2 = ends.pop()
        if len(e2) >= len(e):
            if not e2.endswith(e):
                return "*"
            e = e2
        else:
            if not e.endswith(e2):
                return "*"

    return s + "".join(middles) + e


if __name__ == "__main__":
    t = int(input())  # read number of tests
    for t_i in range(1, t + 1):
        n = int(input())
        pats = [input() for _ in range(n)]
        res = solve(pats, n)
        print("Case #{}: {}".format(t_i, res))
