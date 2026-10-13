class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * (len(nums))
        for i in range(len(nums)):
            res = 1
            for j in range(len(nums)):
                if j == i: continue
                res *= nums[j]
            output[i] = res
        return output
             

