class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        cache = {}
        
        for i in range(len(nums)):
            l, r = 0, 0
            for j in range(len(nums)):
                if j == i:
                    continue
                if j < i:
                    l += nums[j]
                else:
                    r += nums[j]
            if l == r:
                return i
            cache[i] = (l, r)
        return -1

     