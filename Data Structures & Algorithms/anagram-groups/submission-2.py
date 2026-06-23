class Solution:
    def encode_anagram(self, string) -> str:
        freq_map = {}
        for i in string:
            if i not in freq_map:
                freq_map[i] = 0
            freq_map[i] += 1
        return "".join(sorted([str(val)+key for key, val in freq_map.items()]))


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        distinct_strs_map = {}
        for i in strs:
            encoded_str = self.encode_anagram(i)
            if encoded_str not in distinct_strs_map:
                distinct_strs_map[encoded_str] = [i]
            else:
                distinct_strs_map[encoded_str].append(i)
        return list(distinct_strs_map.values())
        