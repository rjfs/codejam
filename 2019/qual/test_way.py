import pytest
import way


@pytest.mark.parametrize(("n", "enemy_path"), [(2, 'SE'), (5, 'EESSSESE'), (3, 'SSEE'), (4, 'EEESSS')])
def test_solve(n, enemy_path):
    path = way.solve(n, enemy_path)
    moves = way.get_path_moves(path)
    enemy_moves = way.get_path_moves(enemy_path)
    assert (path.count('S') == n - 1)
    assert (path.count('E') == n - 1)
    for pos in moves.keys() & enemy_moves.keys():
        assert moves[pos] != enemy_moves[pos]
