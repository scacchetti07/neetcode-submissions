class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for an in strs:
            w = ''.join(sorted(an))
            if w not in anagrams:
                anagrams[w] = []
            anagrams[w].append(an)	

        return list(anagrams.values())