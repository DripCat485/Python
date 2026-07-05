class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def dfs(start, target, path):
            if target == 0:
                res.append(path[:])
                return
            if target < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                path.append(candidates[i])
                dfs(i + 1, target - candidates[i], path)
                path.pop()

        dfs(0, target, [])
        return res