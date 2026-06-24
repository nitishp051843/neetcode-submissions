class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_length = 0
        for i in range(len(s)):
            for j in range(i+1, len(s) + 1):
                length_substr = len(s[i:j])
                if length_substr == len(set(s[i:j])):
                    if max_length < length_substr:
                        max_length = length_substr
        
        return max_length