class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = {}
        start = 0
        long_length = 0

        for index, char in enumerate(s):
            if char in seen and seen[char] >= start:
                start = seen[char] + 1
            seen[char] = index
            long_length = max(long_length, index - start + 1)
        return long_length