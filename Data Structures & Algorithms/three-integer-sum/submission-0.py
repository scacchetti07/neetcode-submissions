class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)
        res = []
        for i, n in enumerate(snums):
            if n > 0:
                break

            if i > 0 and n == snums[i - 1]:
                continue

            l = i + 1
            r = len(snums) - 1
            while l < r:
                sum3 = n + snums[l] + snums[r]
                if sum3 > 0:
                    r -= 1
                if sum3 < 0:
                    l += 1
                if sum3 == 0:
                    res.append([n, snums[l], snums[r]])
                    l += 1
                    r -= 1
                    while snums[l] == snums[l -1] and l < r:
                        l += 1
        return res