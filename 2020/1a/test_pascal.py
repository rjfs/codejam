import pytest
import pascal


class TestSolve:

    triangle = None

    def setup_class(self):
        self.triangle = pascal_triangle(500)

    @pytest.mark.parametrize("s", list(range(1, 30)) + [543446, 752668, 3.234e8] + list(range(int(1e9-100), int(1e9))))
    def test_solve(self, s):
        result = pascal.solve(s)
        assert len(result) <= 500
        assert len(result) == len(set(result))
        res_s = 0
        pi, pj = 0, 0
        for i, j in result:
            res_s += self.triangle[i-1][j-1]
            assert (
                (i, j) in ((pi-1, pj-1), (pi-1, pj), (pi, pj-1), (pi, pj+1), (pi+1, pj), (pi+1, pj+1)),
                "%s > %s" % ((pi, pj), (i, j))
            )
            pi, pj = i, j

        assert res_s == s


def pascal_triangle(n):
    row = [1]
    y = [0]
    values = []
    for x in range(max(n, 0)):
        values.append(row)
        row = [l + r for l, r in zip(row + y, y + row)]
    return values
