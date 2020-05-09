def solve(u, requests):
    # Lower numbers are more likely
    counts = {}
    for r in requests:
        c = r[1][0]
        if c not in counts:
            counts[c] = 1
        else:
            counts[c] += 1

    s_counts = sorted([(k, v) for k, v in counts.items()], key=lambda k: k[1], reverse=True)
    d = {str(i + 1): c[0] for i, c in enumerate(s_counts)}

    # Find 0
    for r in requests:
        for c in r[1]:
            if c not in d.values():
                d["0"] = c
                break

    seq = [d[str(i)][0] for i in range(10)]
    return "".join(seq)


if __name__ == "__main__":
    tc = int(input())  # read number of tests
    for t_i in range(1, tc + 1):
        u = int(input())
        req = [input().split() for _ in range(10**4)]
        print("Case #{}: {}".format(t_i, solve(u, req)))
