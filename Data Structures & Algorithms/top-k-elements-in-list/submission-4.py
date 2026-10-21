class Solution:
    def bucket_sort(self, counter, total):
        buckets = [[] for i in range(total)]
        max_val = max(counter.values())
        for k, v in counter.items():
            normalized = v / (max_val + 1)
            bNo = int(total * normalized)
            buckets[bNo].append([k, v])
        
        for i, bucket in enumerate(buckets):
            if total == 0: continue
            buckets[i] = sorted(bucket)
        
        output = []
        for bucket in buckets:
             output.extend(bucket)

        return output

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        arr = self.bucket_sort(counter, len(nums))
        res = []
        while len(res) < k:
            res.append(arr.pop()[0])
        return res