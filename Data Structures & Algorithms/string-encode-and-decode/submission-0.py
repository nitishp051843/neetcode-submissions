class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        encoded_str = ""
        for item in strs:
            encoded_str += str(len(item)) + "#" + item
        return encoded_str
    def decode(self, s: str) -> List[str]:
        decoded_list = []
        if len(s) == 0:
            return decoded_list
        fptr = 0
        num_str = ""
        while fptr <= len(s) - 1:
            if s[fptr].isdigit():
                num_str += s[fptr]
                fptr += 1
            elif s[fptr] == "#" and num_str != "":
                decoded_list.append(s[fptr+1:fptr+int(num_str)+1])
                fptr += int(num_str) + 1
                num_str = ""
        return decoded_list

