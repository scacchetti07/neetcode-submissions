class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p = []
        for l in zip(*strs):
            if len(set(l)) != 1:
                break
            p.append(l[0])
        return ''.join(p)