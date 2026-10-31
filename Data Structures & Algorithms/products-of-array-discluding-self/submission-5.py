class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    # Solução 2 do Vídeo NeetCode (https://www.youtube.com/watch?v=bNvIQI2wAjk&t)
        p = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            if i - 1 < 0:
                res[i] *= 1
                p *= nums[i]
                continue
            res[i] *= p
            p *= nums[i]

        p = 1
        for i in range(len(nums)-1, -1, -1):
            if i + 1 >= len(nums):
                res[i] *= 1
                p *= nums[i] 
                continue
            res[i] *= p
            p *= nums[i]
    
        return res
            