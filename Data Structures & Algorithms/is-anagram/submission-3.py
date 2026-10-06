class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cache =  {}

        for l in s:
            if l not in cache:
                cache[l] = 1
                continue
            cache[l] += 1

        for l in t:
            if l in cache and cache[l] > 0:
                cache[l] -= 1
            else:
                return False
        return True    