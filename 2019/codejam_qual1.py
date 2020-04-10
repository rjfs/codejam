import time


def four_in_number(i):
    while i:
        if i % 10 == 4:
            return True
        i = i // 10

    return False


def four_digit(n):
    # Returns digit of 4
    # Returns 0 if not found
    n_str = str(n)
    for i_n, i in enumerate(map(int, n_str)):
        if i == 4:
            return len(n_str) - i_n

    return 0


def get_new_i(i, d_i):
    to_add = 5 * 10 ** (d_i - 1)
    to_subtract = int(str(i)[-d_i:])
    return i - to_subtract + to_add


assert get_new_i(4521, 4) == 5000
assert get_new_i(1524, 1) == 1525
assert get_new_i(14521, 4) == 15000


def get_new_j(j, d_j):
    rem_digits = d_j - 1
    if rem_digits > 0:
        to_subtract = int(str(j)[-rem_digits:]) + 1
    else:
        to_subtract = 1

    return j - to_subtract


assert get_new_j(4521, 4) == 3999
assert get_new_j(1524, 1) == 1523
assert get_new_j(14521, 4) == 13999


def find_solution2(n):
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


def find_solution(n):
    i = j = 0
    for i in range(1, n - 1):
        if not four_in_number(i):
            j = n - i
            if not four_in_number(j):
                break
    return i, j


def run_tests():
    tests = [4, 940, 4444]
    tests += [1234568749, 645236459, 94256358956419619189154181 * 10**100000]
    for i_t, n in enumerate(tests):
        assert('4' in str(n))
        t0 = time.time()
        n1, n2 = find_solution2(n)
        t = time.time() - t0
        assert('4' not in str(n1))
        assert ('4' not in str(n2))
        assert (n1 + n2 == n)
        print('Test %d ran in %.2f seconds' % (i_t + 1, t))


run_tests()