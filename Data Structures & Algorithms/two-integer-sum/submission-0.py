class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p1, p2 = 0, 0

        for i in range(len(nums)-1):
            for j in range(len(nums)-1, i, -1):
                if nums[i] + nums[j] != target:
                    continue
                p1 = i
                p2 = j
                break
        return [p1, p2]