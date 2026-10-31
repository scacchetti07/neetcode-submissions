class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    # Solução 2 do Vídeo NeetCode (https://www.youtube.com/watch?v=bNvIQI2wAjk&t)
        pr = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = pr
            pr *= nums[i]
        
        po = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= po
            po *= nums[i]

        return res
            