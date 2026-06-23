class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        if len(s) != len(t):
            return False
        
        counts, countt = Counter(s), Counter(t)

        return counts == countt