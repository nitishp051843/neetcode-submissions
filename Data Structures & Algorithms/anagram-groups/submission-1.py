class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        distinct_strs = {}

        for i in strs:
            tmp = "".join(sorted(i))
            if tmp not in distinct_strs:
                distinct_strs[tmp] = [i]
            else:
                distinct_strs[tmp].append(i)

        return list(distinct_strs.values())        
        