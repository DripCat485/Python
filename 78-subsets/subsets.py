class Solution:
    def subsets(self, nums):
        res = []

        def backtrack(index, path):
            if index == len(nums):
                res.append(path[:])
                return

            backtrack(index + 1, path)

            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

        backtrack(0, [])
        return res