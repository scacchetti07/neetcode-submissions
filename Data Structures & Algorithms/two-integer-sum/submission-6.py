class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(nums)):
            n = nums[i]
            res = target - n
            if res in cache:
                return [cache[res], i]
            cache[n] = i
        return []