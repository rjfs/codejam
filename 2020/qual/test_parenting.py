import pytest
from parenting import find_solution


@pytest.mark.parametrize(
    ("input_str", "result"), [
        (((360, 480), (420, 540), (600, 660)), "CJC"),
        (((0, 1440), (1, 3), (2, 4)), "IMPOSSIBLE"),
        (((99, 150), (1, 100), (100, 301), (2, 5), (150, 250)), "JCCJJ"),
        (((0, 720), (720, 1440)), "CC"),
        (((0, 10), (0, 10), (10, 20), (10, 20)), ""),
        (tuple(), ""),
        (((0, 24 * 60),), "")
    ]
)
def test_example(input_str, result):
    n = len(input_str)
    sol = find_solution(n, input_str)
    if result == "IMPOSSIBLE" or sol == "IMPOSSIBLE":
        assert sol == result

    # Check if solution is valid
    time_v = [""] * 24*60
    for act_n in range(n):
        st, end = input_str[act_n]
        p = sol[act_n]
        for i in range(st, end):
            if p in time_v[i]:
                raise Exception("Solution '%s' not valid" % sol)
            time_v[i] += p
