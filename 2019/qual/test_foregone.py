import pytest
import foregone


@pytest.mark.parametrize(("j", "dj", "result"), [(4521, 4, 3999), (1524, 1, 1523), (14521, 4, 13999)])
def test_get_new_j(j, dj, result):
    assert foregone.get_new_j(j, dj) == result


@pytest.mark.parametrize(("i", "di", "result"), [(4521, 4, 5000), (1524, 1, 1525), (14521, 4, 15000)])
def test_get_new_i(i, di, result):
    assert foregone.get_new_i(i, di) == result


@pytest.mark.parametrize("n", [4, 940, 4444, 1234568749, 645236459, 4444*10**99])
def test_solve(n):
    assert '4' in str(n)
    n1, n2 = foregone.solve(n)
    assert '4' not in str(n1)
    assert '4' not in str(n2)
    assert n1 + n2 == n
