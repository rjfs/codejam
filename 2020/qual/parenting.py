import bisect


def find_solution(n, activities):
    busy = [0] * (24*60 + 1)  # number of activities for each minute - max should be 2
    sorted_acts = []
    for act_n in range(n):
        st, end = activities[act_n]
        act = Activity(act_n, st, end)
        for i in range(st, end):
            if busy[i] == 2:
                # 3 activities at the same time
                return "IMPOSSIBLE"
            busy[i] += 1
        bisect.insort_left(sorted_acts, act)

    end_j = 0
    output = ["J"] * n
    while sorted_acts:
        act = sorted_acts.pop(0)
        if act.start >= end_j:
            end_j = act.end
        else:
            output[act.n] = "C"

    return "".join(output)


class Activity:

    def __init__(self, n, start, end):
        self.n = n
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.start < other.start


def std_in_out():
    t = int(input())  # read number of tests
    for t_i in range(1, t + 1):
        N = int(input())
        lists = [tuple(int(i) for i in input().split()) for _ in range(N)]
        res = find_solution(N, lists)
        print("Case #{}: {}".format(t_i, res))


if __name__ == "__main__":
    std_in_out()
