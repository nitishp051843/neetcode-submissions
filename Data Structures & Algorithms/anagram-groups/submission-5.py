class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for val in strs:
            key = tuple(sorted(val))
            if key in mapping:
                mapping[key].append(val)
            else:
                mapping[key] = [val]
        
        return list(mapping.values())
