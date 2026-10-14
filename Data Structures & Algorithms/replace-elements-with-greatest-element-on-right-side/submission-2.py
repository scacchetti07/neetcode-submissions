class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        for i in range(len(arr)):
            if i+1 >= len(arr):
                ans.append(-1)
                break
            hi = max(arr[i+1:])
            ans.append(hi)
        return ans