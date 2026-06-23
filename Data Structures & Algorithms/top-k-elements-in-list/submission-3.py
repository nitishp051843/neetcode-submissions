class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for i in nums:
            counter[i] = counter.get(i, 0) + 1
        
        sorted_mapping = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))

        return list(sorted_mapping.keys())[:k]