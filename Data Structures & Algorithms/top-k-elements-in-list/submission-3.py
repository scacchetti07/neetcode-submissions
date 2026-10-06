class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = Counter(nums)
        res = []
        for k, v in n.most_common(k):
            res.append(k)
        
        return res