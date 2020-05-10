def four_digit(n):
    """ Returns digit of 4. Returns 0 if not found """
    n_str = str(n)
    for i_n, i in enumerate(map(int, n_str)):
        if i == 4:
            return len(n_str) - i_n

    return 0


def get_new_i(i, d_i):
    to_add = 5 * 10 ** (d_i - 1)
    to_subtract = int(str(i)[-d_i:])
    return i - to_subtract + to_add


def get_new_j(j, d_j):
    rem_digits = d_j - 1
    if rem_digits > 0:
        to_subtract = int(str(j)[-rem_digits:]) + 1
    else:
        to_subtract = 1

    return j - to_subtract


def solve(n):
    i = 1
    while True:
        d_i = four_digit(i)
        if d_i == 0:
            j = n - i
            d_j = four_digit(j)
            if d_j == 0:
                break
            else:
                j = get_new_j(j, d_j)
                i = n - j
        else:
            i = get_new_i(i, d_i)

    return i, j


if __name__ == "__main__":
    t = int(input())  # read a line with a single integer
    for ti in range(1, t + 1):
        N = int(input())
        n1, n2 = solve(N)
        print("Case #{}: {} {}".format(ti, n1, n2))
