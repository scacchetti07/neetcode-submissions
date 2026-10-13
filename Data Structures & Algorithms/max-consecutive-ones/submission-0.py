class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        vals = []
        s = 0
        for n in nums:
            if n == 0:
                vals.append(s)
                s = 0
            else:
                s += 1
        
        if s > 0:
            vals.append(s)

        return max(vals)