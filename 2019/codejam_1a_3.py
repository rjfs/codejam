# Alien Rhyme
import time


def get_terms(words, i=1):
    terms = {}
    print('---')
    print(words)
    print(i)
    for w in words:
        t = w[-i]
        if t not in terms:
            terms[t] = set()
        terms[t].add(w)

    print(terms)
    return terms


def get_n_groups(words, i=1):
    if len(words) == 1:
        return 0, 1
    else:
        childs = [
            get_n_groups(child_words, i=i+1)
            for child, child_words in get_terms(words, i=i).items()
        ]
        # Group
        childs = [
            (gr, ungr) if ungr <= 1 else (gr + 2, ungr - 2)
            for gr, ungr in childs
        ]
        n_ungrouped = sum(i[1] for i in childs)
        n_grouped = sum(i[0] for i in childs)
        return n_grouped, n_ungrouped


def find_solution(words):
    return get_n_groups(words)[0]


def run_tests():
    tests = [
        (('A', 'B'), 0),
        (('A', 'A'), 2),
        (('TARPOL', 'PROL'), 2),
        (('TARPOR', 'PROL', 'TARPRO'), 0),
        ({'CODEJAM', 'JAM', 'HAM', 'NALAM', 'HUM', 'NOLOM'}, 6),
        ({'PI', 'HI', 'WI', 'FI'}, 2),
        (tuple('P%sS' % i for i in range(1000)), 222),
        (tuple('P%s_END' % i for i in range(1000)), 228),
        (('', ''), 0),
    ]
    for i_t, (words, expected_res) in enumerate(tests):
        t0 = time.time()
        res = find_solution(words)
        t = time.time() - t0
        print(words, res)
        assert res == expected_res
        print('Test %d ran in %.2f seconds' % (i_t + 1, t))


def std_in_out():
    t = int(input())  # read number of tests
    for t_i in range(1, t + 1):
        n_words = int(input())  # read number of words
        words = [input() for _ in range(n_words)]
        res = find_solution(words)
        print("Case #{}: {}".format(t_i, res))


run_tests()
