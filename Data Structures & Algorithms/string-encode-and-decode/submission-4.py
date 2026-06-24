class Solution:

    def encode(self, strs: List[str]) -> str:
        sep = "#"
        encoded_str = ""
        for i in strs:
            encoded_str += str(len(i)) + sep + i
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []

        index = 0
        curr_num = ""
        while index < len(s):
            if s[index].isdigit():
                curr_num += s[index]
            elif s[index] == "#":
                decoded_strs.append(s[index+1: index+int(curr_num)+1])
                index += int(curr_num)
                curr_num = ""
            index += 1
        
        return decoded_strs