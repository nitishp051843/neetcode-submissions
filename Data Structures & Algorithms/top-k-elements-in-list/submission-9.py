from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1 )]

        for num, freq in counts.items():
            buckets[freq].append(num)
        
        result = []

        for index in range(len(buckets)-1, 0, -1):
            bucket = buckets[index]
            if bucket and len(bucket) <= k:
                result.extend(bucket)
                k -= len(bucket)
            
            if k == 0:
                return result
        return result
