def find_solution(digits):
    c = 0
    output = ""
    for d_str in digits:
        d = int(d_str)
        while c < d:
            output += "("
            c += 1
        while c > d:
            output += ")"
            c -= 1

        output += d_str

    while c > 0:
        output += ")"
        c -= 1

    return output


def std_in_out():
    t = int(input())  # read number of tests
    for t_i in range(1, t + 1):
        res = find_solution(input())
        print("Case #{}: {}".format(t_i, res))


if __name__ == "__main__":
    std_in_out()
