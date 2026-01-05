def peak_find(A, start: int = 0, end: int | None = None):
    if end is None:
        end = len(A)
    if start >= end:
        return None
    i = (start + end) // 2
    left = A[i - 1] if i - 1 >= 0 else float("-inf")
    right = A[i + 1] if i + 1 < len(A) else float("-inf")
    if left <= A[i] >= right:
        return (i, A[i])
    if left > A[i]:
        return peak_find(A, start, i)
    return peak_find(A, i + 1, end)


if __name__ == "__main__":
    tests = [
        [1, 2, 6, 5, 3, 7, 4],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1],
        [1,2]
    ]
    for t in tests:
        print(t, "->", peak_find(t))
