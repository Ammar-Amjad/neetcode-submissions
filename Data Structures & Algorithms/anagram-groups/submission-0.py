
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for idx, word in enumerate(strs):
            word_sorted = "".join(sorted(word))
            if word_sorted not in dic:
                dic[word_sorted] = [word]
            else:
                dic[word_sorted] += [word]
        
        res = []
        for k, v in dic.items():
            res.append(v)

        return res
        

