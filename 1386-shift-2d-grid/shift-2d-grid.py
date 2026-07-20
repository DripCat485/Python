class Solution:
    def shiftGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total

        arr = []
        for row in grid:
            arr.extend(row)

        arr = arr[-k:] + arr[:-k]

        res = []
        for i in range(0, total, n):
            res.append(arr[i:i + n])

        return res