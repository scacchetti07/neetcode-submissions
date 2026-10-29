class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cache = defaultdict(int)
        for i, n in enumerate(numbers):
            if i + 1 >= len(numbers):
                break
            res = n + numbers[i+1]
            cache[res] = i
        
        if target in cache.keys():
            return [cache[target]+1, cache[target]+2]

        return []