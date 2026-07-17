from bisect import bisect_right

class Solution:
    def gcdValues(self, nums, queries):
        mx = max(nums)
        freq = [0] * (mx + 1)

        for x in nums:
            freq[x] += 1

        exact = [0] * (mx + 1)

        for g in range(mx, 0, -1):
            cnt = 0
            for k in range(g, mx + 1, g):
                cnt += freq[k]
            pairs = cnt * (cnt - 1) // 2
            m = 2 * g
            while m <= mx:
                pairs -= exact[m]
                m += g
            exact[g] = pairs

        prefix = []
        values = []
        s = 0
        for g in range(1, mx + 1):
            if exact[g]:
                s += exact[g]
                prefix.append(s)
                values.append(g)

        ans = []
        for q in queries:
            ans.append(values[bisect_right(prefix, q)])
        return ans