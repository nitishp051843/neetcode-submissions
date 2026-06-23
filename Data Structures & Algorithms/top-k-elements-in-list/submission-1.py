from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for i in nums:
            freq_map[i] += 1

        sorted_items = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]