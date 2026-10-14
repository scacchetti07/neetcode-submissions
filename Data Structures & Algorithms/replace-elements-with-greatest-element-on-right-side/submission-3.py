class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        hi = -1
        ans = []
        for i in range(len(arr)):
            hi = -1
            for j in range(i+1, len(arr)):
                if hi < arr[j]:
                    hi = arr[j]
            if i+1 < len(arr):
                ans.append(hi)
            else:
                ans.append(-1)
        return ans
            
        