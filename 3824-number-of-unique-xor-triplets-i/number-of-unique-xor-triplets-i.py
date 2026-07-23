class Solution:
    def uniqueXorTriplets(self, nums):
        n = len(nums)
        if n == 1:
            return 1
        if n == 2:
            return 2
        return 1 << n.bit_length()