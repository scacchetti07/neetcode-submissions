class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Solução 1 do Vídeo NeetCode (https://www.youtube.com/watch?v=bNvIQI2wAjk&t)
        left  = [1] * len(nums)
        right = [1] * len(nums)
        output = []
        p = len(nums) - 1
        for i in range(len(nums)):
            if i == 0:
                left[i] = nums[i]
                right[p] = nums[p]
                p -= 1
                continue
            
            if i - 1 >= 0:
                left[i] = left[i - 1] * nums[i]
            if i + 1 < len(nums):
                right[p] = right[p + 1] * nums[p]
            
            p -= 1
        
        for i in range(len(nums)):
            if i - 1 < 0:
                output.append(1 * right[i+1])
            elif i + 1 >= len(nums):
                output.append(1 * left[i-1])
            else:
                output.append(left[i-1] * right[i+1])
        
        return output








            
