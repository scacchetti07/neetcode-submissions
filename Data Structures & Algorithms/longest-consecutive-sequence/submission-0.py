class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        output = []
        for n in nums:
            if len(output) == 0:
                output.append(n)
                continue
            if (output[-1] - n) in [1, -1]:
                output.append(n)
        return len(output)