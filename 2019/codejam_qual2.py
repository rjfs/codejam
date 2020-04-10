import time


def move(pos, direction):
    if direction == 'E':
        return pos[0], pos[1] + 1
    else:
        return pos[0] + 1, pos[1]


def get_new_move(pos, enemy_moves, strategy):
    if pos in enemy_moves.keys():
        new_move = 'E' if enemy_moves[pos] == move(pos, 'S') else 'S'
    else:
        if strategy == 'U':
            new_move = 'E'
        else:
            new_move = 'S'

    return new_move


def find_solution(n, enemy_path):
    # Simulator
    path = ''
    pos = (1, 1)
    enemy_pos = (1, 1)
    enemy_moves = get_path_moves(enemy_path)
    i = 0
    strategy = 'U' if (n, n - 1) in enemy_moves.keys() else 'D'
    while pos != (n, n):
        if strategy == 'D' and pos[0] > enemy_pos[0]:
            new_move = 'S' if pos[0] != n else 'E'
        elif strategy == 'U' and pos[1] > enemy_pos[1]:
            new_move = 'E' if pos[1] != n else 'S'
        else:
            new_move = get_new_move(pos, enemy_moves, strategy)

        # Update
        path += new_move
        pos = move(pos, new_move)
        enemy_pos = move(enemy_pos, enemy_path[i])
        assert pos[0] <= n
        assert pos[1] <= n
        i += 1

    return path


def get_path_moves(path):
    moves = {}
    pos = (1, 1)
    for c in path:
        if c == 'S':
            new_pos = (pos[0] + 1, pos[1])
        else:
            new_pos = (pos[0], pos[1] + 1)

        moves[pos] = new_pos
        pos = new_pos

    return moves


def run_tests():
    tests = [(2, 'SE'), (5, 'EESSSESE')]
    tests += [(3, 'SSEE'), (4, 'EEESSS')]
    for i_t, (n, enemy_path) in enumerate(tests):
        t0 = time.time()
        path = find_solution(n, enemy_path)
        print(enemy_path, path)
        t = time.time() - t0
        moves = get_path_moves(path)
        enemy_moves = get_path_moves(enemy_path)
        assert(path.count('S') == n - 1)
        assert(path.count('E') == n - 1)
        for pos in moves.keys() & enemy_moves.keys():
            assert moves[pos] != enemy_moves[pos]
        print('Test %d ran in %.2f seconds' % (i_t + 1, t))


run_tests()
