def solve(x, y):
    d = abs(x) + abs(y)
    if not d % 2:
        return "IMPOSSIBLE"

    sol_abs = solve_abs(abs(x), abs(y))
    sol = ""
    for c in sol_abs:
        if x < 0 and c in {"W", "E"}:
            sol += "W" if c == "E" else "E"
        elif y < 0 and c in {"S", "N"}:
            sol += "S" if c == "N" else "N"
        else:
            sol += c

    return sol


def solve_abs(x, y):
    """ Solve problem for x and y positive """
    sol = ""
    i = 0
    while x > 1 or y > 1:
        i += 1
        if x % 2:
            # Either W or E
            if ((x + 1) // 2 + y // 2) % 2:
                sol += "W"
                x = (x + 1) // 2
            else:
                sol += "E"
                x = (x - 1) // 2

            y //= 2
        else:
            # Either S or N
            if ((y + 1) // 2 + x // 2) % 2:
                sol += "S"
                y = (y + 1) // 2
            else:
                sol += "N"
                y = (y - 1) // 2

            x //= 2

    # Last step
    if not x:
        sol += "N" if y == 1 else "S"
    else:
        sol += "E" if x == 1 else "W"

    return sol


if __name__ == "__main__":
    t = int(input())  # read number of tests
    for t_i in range(1, t + 1):
        res = solve(*[int(i) for i in input().split()])
        print("Case #{}: {}".format(t_i, res))
