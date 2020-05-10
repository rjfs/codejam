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


def solve(n, enemy_path):
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


if __name__ == "__main__":
    nt = int(input())  # read a line with a single integer
    for ti in range(1, nt + 1):
        N = int(input())
        ep = input()
        print("Case #{}: {}".format(ti, solve(N, ep)))
