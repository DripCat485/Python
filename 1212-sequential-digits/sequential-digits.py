class Solution:
    def sequentialDigits(self, low, high):
        s = "123456789"
        res = []

        for length in range(len(str(low)), len(str(high)) + 1):
            for i in range(10 - length):
                num = int(s[i:i + length])
                if low <= num <= high:
                    res.append(num)

        return res