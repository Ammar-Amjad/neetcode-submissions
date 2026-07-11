class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]: 
        
        res = []

        def dfs(i, List):
            if len(List) == k:
                res.append(List)
                return

            for j in range(i, n + 1):
                dfs(j + 1, List + [j])

        dfs(1, [])
        return res
