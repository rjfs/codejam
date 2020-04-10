import pytest
from vestigium import find_solution


@pytest.mark.parametrize(
    ("input_str", "result"), [
        (((1, 2, 3, 4), (2, 1, 4, 3), (3, 4, 1, 2), (4, 3, 2, 1)), "4 0 0"),
        (((2, 2, 2, 2), (2, 3, 2, 3), (2, 2, 2, 3), (2, 2, 2, 2)), "9 4 4"),
        (((2, 1, 3), (1, 3, 2), (1, 2, 3)), "8 0 2"),
        (((1, 1), (1, 1)), "2 2 2"),
        (tuple(), "0 0 0"),
    ]
)
def test_example(input_str, result):
    n = len(input_str)
    assert find_solution(n, input_str) == result