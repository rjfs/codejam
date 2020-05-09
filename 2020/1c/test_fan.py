import pytest
import fan


@pytest.mark.parametrize(
    ("x", "y", "m", "solution"), [
        (4, 4, "SSSS", 4),
        (3, 0, "SNSS", "IMPOSSIBLE"),
        (2, 10, "NSNNSN", "IMPOSSIBLE"),
        (0, 1, "S", 1),
        (2, 7, "SSSSSSSS", 5),
        (3, 2, "SSSW", 4),
        (4, 0, "NESW", 4),
    ]
)
def test_solve(x, y, m, solution):
    assert fan.solve(x, y, m) == solution
