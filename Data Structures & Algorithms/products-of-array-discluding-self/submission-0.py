class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        i = 0
        while i < len(nums):
            curr = nums[i]
            res = 1
            for n in nums:
                if curr == n: continue
                res *= n
            output.append(res)
            i += 1
        return output 
             

