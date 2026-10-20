class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}

        for i in range(len(nums)-1, -1, -1):
            c = target - nums[i]
            if nums[i] in vals:
                return [i, vals[nums[i]]]
            vals[c] = i
        return []