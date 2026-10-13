class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        for i in range(k):
            if nums[i] == val:
                nums[i] = None
                k -= 1

        while None in nums:
            nums.remove(None)
        return k