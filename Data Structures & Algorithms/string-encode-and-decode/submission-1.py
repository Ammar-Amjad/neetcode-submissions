class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for Str in strs:
            s += str(len(Str)) + "$" + Str
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        
        i = 0
        res = []

        while i < len(s):
            str_len = ""
            
            while s[i] != "$":
                str_len += s[i]
                i += 1

            str_len_int = int(str_len)
            word_num = 'word'
            i += 1

            
            single_str = s[i: i + str_len_int]
            res += [single_str]
             
            i += str_len_int
            
        return res 