class Solution:
    def generateParenthesis(self, n):
        res = []

        def backtrack(cur, open_count, close_count):
            if len(cur) == 2 * n:
                res.append(cur)
                return

            if open_count < n:
                backtrack(cur + "(", open_count + 1, close_count)

            if close_count < open_count:
                backtrack(cur + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return res