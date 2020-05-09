def solve(x, y, m):
    d = abs(x) + abs(y)
    if d == 0:
        return 0

    t = 0
    for move in m:
        if move == "S":
            y -= 1
        elif move == "N":
            y += 1
        elif move == "W":
            x -= 1
        else:
            x += 1
        d = abs(x) + abs(y)
        t += 1
        if t >= d:
            return t

    return "IMPOSSIBLE"


if __name__ == "__main__":
    T = int(input())  # read number of tests
    for t_i in range(1, T + 1):
        line = input().split()
        res = solve(int(line[0]), int(line[1]), line[2])
        print("Case #{}: {}".format(t_i, res))
