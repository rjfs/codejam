# Alien Rhyme
import time
import pprint


def find_pairs(w, words):
    pairs = {}
    for w2 in words:
        i = -1
        j = -1 - i  # count char from the end
        d_set = set()
        min_len = min(len(w), len(w2))
        while j < min_len and w[i] == w2[i]:
            d_set.add(j)
            # update i and j
            i -= 1
            j = -1 - i

        if len(d_set) > 0:
            pairs[w2] = d_set

    return pairs


def get_decreased_dict(d, a, b, i):
    decreased_dict = d.copy()
    decreased_dict.pop(a, None)
    decreased_dict.pop(b, None)
    return {
        k: {k2: v2 for k2, v2 in v.items() if not (k2 in (a, b) and v2 == i)}
        for k, v in decreased_dict.items()
    }


def get_decreased_dict2(d, a, b):
    out = {
        k: set(i for i in v if i not in (a, b))
        for k, v in d.items()
        if k not in (a, b)
    }
    return {k: v for k, v in out.items() if len(v) > 0}


def foo(d):
    # TODO: N
    solutions = []
    prev_size = -1
    while len(solutions) > prev_size:
        prev_size = len(solutions)
        curr_sol = set()
        while len(d) > 0:
            a = set(d.keys()).pop()
            b = d[a].pop()
            curr_sol.add((a, b))
            d = get_decreased_dict2(d, a, b)

        if len(curr_sol) > 0:
            solutions.append(curr_sol)

    return solutions


def get_decreased_dict3(d, a, b, i):
    print('----')
    pprint.pprint(d)
    print(a, b, i)
    out = {}
    for k, vals_d in d.items():
        if k not in (a, b):
            d_in = {
                k_in: set([
                    v_in for v_in in v
                    if not ((a in k_in and i == v_in) or (b in k_in and i == v_in))
                ])
                for k_in, v in vals_d.items()
                if k_in not in (a, b)
            }
            d_in = {k3: v3 for k3, v3 in d_in.items() if len(v3) > 0}
            if len(d_in) > 0:
                out[k] = d_in

    pprint.pprint(out)

    return out


def get_decreased_dict4(d, A, B, I):
    print('---')
    pprint.pprint(d)
    print(A, B, I)
    out = {}
    for a, v in d.items():
        for b, i_set in v.items():
            if a not in (A, B) and b not in (A, B):
                for i in i_set:
                    cond1 = i in d.get(A, {}).get(a, set()) and len(d.get(A, {}).get(a, set())) > 0
                    cond2 = i in d.get(B, {}).get(b, set()) and len(d.get(B, {}).get(b, set())) > 0
                    if i != I or (not cond1 and not cond2):
                        # add
                        if a not in out.keys():
                            out[a] = {}
                        if b not in out[a].keys():
                            out[a][b] = set()
                        out[a][b].add(i)

    pprint.pprint(out)
    return out


def get_decreased_dict5(d, A, B, I):
    out = {}
    for a, v1 in d.items():
        for b, v2 in v1.items():
            if a not in (A, B) and b not in (A, B):
                for i in v2:
                    cond1 = i not in d[A].get(a, set())
                    cond2 = i not in d.get(a, {}).get(A, set())
                    if i != I or (cond1 and cond2):
                        # add
                        if a not in out.keys():
                            out[a] = {}
                        if b not in out[a].keys():
                            out[a][b] = set()
                        out[a][b].add(i)

    return out


def foo2(d):
    # TODO: N
    solutions = []
    prev_size = -1
    while len(solutions) > prev_size:
        prev_size = len(solutions)
        curr_sol = set()
        while len(d) > 0:
            a = list(d.keys())[0]
            b = list(d[a].keys())[0]
            i = list(d[a][b])[0]
            curr_sol.add((a, b))
            d = get_decreased_dict5(d, a, b, i)

        if len(curr_sol) > 0:
            solutions.append(curr_sol)

    return solutions


def foo3(d):
    # TODO: N
    # Get list of tuples
    elems = set()
    for a, v in d.items():
        for b, i_lst in v.items():
            for i in i_lst:
                elems.add((a, b, i))

    return get_solutions(elems)


def cut_elems(e, elems):
    return elems


def solution(trigger, d, sol=None):
    if sol is None:
        a, b, i = trigger
        sol = {(a, b)}
        d = get_decreased_dict5(d, a, b, i)

    while len(d) > 0:
        a = list(d.keys())[0]
        b = list(d[a])[0]
        i = list(d[a][b])[0]
        d = get_decreased_dict5(d, a, b, i)
        sol.add((a, b))
        sol = solution(trigger=(a, b, i), d=d, sol=sol)

    return sol


def get_solutions(d):
    solutions = []
    for k1, v1 in d.items():
        for k2, v2 in v1.items():
            for i in v2:
                trigger = (k1, k2, i)
                solutions.append(solution(trigger, d))
                print('----')
                print(trigger)
                print(solution(trigger, d))
    aaa

    return solutions


def find_solution(words):
    words_pairs = {}
    for i, w in enumerate(words):
        p = find_pairs(w, list(words)[i + 1:])
        if len(p) > 0:
            words_pairs[w] = p

    solutions = get_solutions(words_pairs)

    for s in solutions:
        print(s)
    aaa

    l = 0
    bs = set()
    for s in solutions:
        if len(s) > l:
            l = len(s)
            bs = s

    print(bs)
    time.sleep(1)
    aaa

    return bs


def run_tests():
    tests = [
        # (('TARPOL', 'PROL'), 2),
        # (('TARPOR', 'PROL', 'TARPRO'), 0),
        (('CODEJAM', 'JAM', 'HAM', 'NALAM', 'HUM', 'NOLOM'), 6),
        (('PI', 'HI', 'WI', 'FI'), 2)
    ]
    for i_t, (words, expected_res) in enumerate(tests):
        t0 = time.time()
        pairs = find_solution(words)
        t = time.time() - t0
        print(pairs)
        print(len(pairs) * 2, expected_res)
        assert len(pairs) * 2 == expected_res
        # for i in largest_subset:
        #     assert i in words
        print('Test %d ran in %.2f seconds' % (i_t + 1, t))


run_tests()
