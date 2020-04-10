import pytest
from nesting import find_solution


@pytest.mark.parametrize(
    ("input_str", "result"), [
        ("021", "0((2)1)"),
        ("312", "(((3))1(2))"),
        ("4", "((((4))))"),
        ("221", "((22)1)"),
        ("0000", "0000"),
        ("101", "(1)0(1)"),
        ("111000", "(111)000"),
        ("1", "(1)"),
        ("", "")
    ]
)
def test_example(input_str, result):
    assert find_solution(input_str) == result
