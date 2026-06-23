class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        if len(s) != len(t):
            return False
        
        counts, countt = Counter(s), Counter(t)

        for i in counts:
            if i not in t:
                return False

            if counts[i] != countt[i]:
                return False
            
        return True