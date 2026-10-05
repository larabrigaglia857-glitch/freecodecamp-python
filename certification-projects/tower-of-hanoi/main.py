def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    moves = []

    def solve(n, source, target, auxiliary):
        if n == 0:
            return

        # Move n - 1 disks from source to auxiliary
        solve(n - 1, source, auxiliary, target)

        # Move the largest disk from source to target
        rods[target].append(rods[source].pop())
        moves.append(" ".join(str(rod) for rod in rods))

        # Move n - 1 disks from auxiliary to target
        solve(n - 1, auxiliary, target, source)

    moves.append(" ".join(str(rod) for rod in rods))
    solve(n, 0, 2, 1)

    return "\n".join(moves)