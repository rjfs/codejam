import pytest
import expogo


@pytest.mark.parametrize(
    ("n", "result"), [
        (0, tuple()),
        (1, (1,)),
        (2, (2,)),
        (3, (1, 2)),
        (5, (1, 4)),
        (12, (8, 4)),
        (15, (1, 2, 4, 8)),
    ]
)
def _test_decompose(n, result):
    assert set(expogo.decompose(n)) == set(result)


@pytest.mark.parametrize(
    ("x", "y", "len_result", "is_possible"), [
        (2, 3, 3, True),
        (3, 2, 3, True),
        (-2, -3, 3, True),
        (-3, -2, 3, True),
        (3, 0, 2, True),
        (0, 3, 2, True),
        (-1, 1, -1, False),
        (0, 4, -1, False),
        (16, 32, -1, False),
        (2, 5, 3, True),
        (5, 2, 3, True),
        (1, 4, 3, True),
        (4, 1, 3, True),
    ]
)
def test_solve(x, y, len_result, is_possible):
    sol = expogo.solve(x, y)
    print("solution: %s" % sol)
    if not is_possible:
        assert sol == "IMPOSSIBLE"
    else:
        assert len(sol) == len_result
        sx, sy = 0, 0
        for i, s in enumerate(sol):
            n = 2 ** i
            if s == "S":
                sy -= n
            elif s == "N":
                sy += n
            elif s == "W":
                sx -= n
            elif s == "E":
                sx += n
        assert (x, y) == (sx, sy)
