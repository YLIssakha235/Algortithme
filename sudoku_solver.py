from typing import List, Optional, Set


def row_indices(n: int) -> List[int]:
    r = n // 9
    return [r * 9 + i for i in range(9)]


def col_indices(n: int) -> List[int]:
    c = n % 9
    return [c + 9 * i for i in range(9)]


def block_indices(n: int) -> List[int]:
    r = (n // 9) // 3 * 3
    c = (n % 9) // 3 * 3
    return [ (r + dr) * 9 + (c + dc) for dr in range(3) for dc in range(3) ]


def blacklist(grid: List[int], n: int) -> Set[int]:
    used = set()
    for i in row_indices(n) + col_indices(n) + block_indices(n):
        v = grid[i]
        if v != 0:
            used.add(v)
    return used


def candidates(grid: List[int], n: int) -> Set[int]:
    return set(range(1,10)) - blacklist(grid, n)


def find_empty_positions(grid: List[int]) -> List[int]:
    return [i for i, v in enumerate(grid) if v == 0]


def solve(grid: List[int]) -> Optional[List[int]]:
    empties = find_empty_positions(grid)
    if not empties:
        return grid

    best = None
    best_cands: Set[int] = set()
    for pos in empties:
        cands = candidates(grid, pos)
        if not cands:
            return None
        if best is None or len(cands) < len(best_cands):
            best = pos
            best_cands = cands
            if len(best_cands) == 1:
                break

    assert best is not None
    for val in sorted(best_cands):
        grid_copy = grid.copy()
        grid_copy[best] = val
        solved = solve(grid_copy)
        if solved is not None:
            return solved
    return None


if __name__ == "__main__":
    example = [
        5,3,0,0,7,0,0,0,0,
        6,0,0,1,9,5,0,0,0,
        0,9,8,0,0,0,0,6,0,
        8,0,0,0,6,0,0,0,3,
        4,0,0,8,0,3,0,0,1,
        7,0,0,0,2,0,0,0,6,
        0,6,0,0,0,0,2,8,0,
        0,0,0,4,1,9,0,0,5,
        0,0,0,0,8,0,0,7,9
    ]

    sol = solve(example)
    print("Solved:")
    if sol is None:
        print("No solution")
    else:
        for r in range(9):
            row = sol[r*9:(r+1)*9]
            print(row)
