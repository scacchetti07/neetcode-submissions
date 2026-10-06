class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = {}
        r = False
        for n in nums:
            if n in vals.keys():
                r = True
                break
            vals[n] = 1
        return r
        
        
            
