class Solution:
    def search(self, nums: List[int], target: int) -> int:
        h = len(nums)-1
        l = 0

        while h >= l:
            p = (h + l) // 2

            if nums[p] == target:
                return p
            
            if target > nums[p]:
                l += 1
            else:
                h -= 1
        return -1       