class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        Res = set()

        def dfs(i, currSet):
            Res.add(currSet)

            for j in range(i, len(nums)):
                if nums[j] not in Res:
                    dfs(j + 1, currSet + (nums[j],) )
            return

        dfs(0, ())
        return [list(r) for r in Res]