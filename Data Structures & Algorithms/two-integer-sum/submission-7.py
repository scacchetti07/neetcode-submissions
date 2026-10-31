class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in res:
                return [i, res[diff]]
            res[nums[i]] = i
        return []
