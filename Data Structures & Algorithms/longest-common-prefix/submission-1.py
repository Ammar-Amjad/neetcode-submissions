class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0] 
        res = ""
        first_word = strs[0]
        if first_word == "": return res
        for idx_char in range(len(first_word)):
            for word_idx in range(1, len(strs)):
                curr_word = strs[word_idx]
                if idx_char >= len(curr_word): return res
                if first_word[idx_char] != curr_word[idx_char]: return res
            res += first_word[idx_char]
        return res